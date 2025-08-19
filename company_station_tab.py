# -*- coding: utf-8 -*-
"""
公司站点数据看板模块
功能：展示和处理公司提供的极地站点数据
Created on Fri Aug  8 14:04:35 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st  # Web应用框架
import os  # 操作系统接口
import datetime  # 日期时间处理
import pandas as pd  # 数据处理库
from utils.process_company_data import process_company_data  # 数据处理工具
from utils.display_data_table import display_data_table  # 数据展示工具
from utils.render_plots import render_plots  # 图表渲染工具

def company_station_tab(current_date: datetime.datetime):
    """
    公司站点数据看板标签页
    参数:
        current_date (datetime): 当前日期时间
    """
    st.title("公司极地数据看板")
    path = './station/公司站点数据'
    
    # 获取子文件夹列表
    subfolder = [item for item in os.listdir(path) 
                if os.path.isdir(os.path.join(path, item))]
    
    if subfolder:
        # 创建水平单选按钮选择数据类型
        option = st.radio("选择数据类型：", os.listdir(path), horizontal=True)
    else:
        st.info("当前无公司数据")
        return
    
    # 选择时间粒度
    data_type = st.selectbox("请选择时间粒度", ("逐小时数据", "月平均"), index=0)
    
    # 处理公司数据
    df, start_time, end_time = process_company_data(option)
    
    # 创建日期范围选择器
    col21, col22, col23 = st.columns([1, 0.1, 1])
    with col21:
        start_date = st.date_input("请选择开始日期", value=start_time, 
                                  min_value=start_time, 
                                  max_value=end_time)
    with col22:
        st.markdown("—", help="日期范围分隔符")
    with col23:
        end_date = st.date_input("请选择结束日期", value=end_time, 
                                min_value=start_date, 
                                max_value=end_time)
    
    # 转换日期格式并过滤数据
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_df = df[(df['观测时间'] >= start_date) & (df['观测时间'] <= end_date)]
    
    # 根据选择的时间粒度处理数据
    if data_type == "月平均":
        # 按月分组计算平均值
        monthly_avg = filtered_df.groupby([filtered_df["观测时间"].dt.year, 
                                          filtered_df["观测时间"].dt.month]).mean()
        monthly_avg.index.names = ['年份', '月份']
        
        # 删除不需要的列
        monthly_avg = monthly_avg.drop(columns=['观测时间', "到报时间"], errors='ignore')
        
        # 创建日期索引
        monthly_avg['日期'] = pd.to_datetime(
            monthly_avg.index.get_level_values('年份').astype(str) + '-' +
            monthly_avg.index.get_level_values('月份').astype(str) + '-01'
        )
        monthly_avg = monthly_avg.set_index('日期')
        monthly_avg.index = monthly_avg.index.strftime('%Y-%m')
    else:
        # 使用原始时间戳数据
        filtered_df.set_index('观测时间', inplace=True)
        monthly_avg = filtered_df
    
    # 展示数据表格和图表
    display_data_table(monthly_avg)
    render_plots(monthly_avg)