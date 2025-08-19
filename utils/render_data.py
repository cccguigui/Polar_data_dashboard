# -*- coding: utf-8 -*-
"""
数据渲染模块
功能：渲染站点数据并提供交互式可视化
Created on Fri Aug  8 14:04:17 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st
import datetime
import pandas as pd
from utils.process_data import process_data
from utils.display_data_table import display_data_table
from utils.render_plots import render_plots
from utils.feature_plots import feature_plots

def render_data(selected_station, current_date: datetime.datetime):
    """
    渲染站点数据
    参数:
        selected_station (str): 选中的站点名称
        current_date (datetime): 当前日期
    """
    # 选择数据类型
    data_type = st.selectbox("请选择查看数据类型", ("多年月平均", "年平均", "月平均"), index=0)
    excel_path = "./station/" + selected_station + ".xlsx"
    df = pd.read_excel(excel_path, engine='openpyxl')
    
    if data_type == "月平均":
        # 月平均数据界面
        col21, col22, col23 = st.columns([1, 0.1, 1])
        with col21:
            start_date = st.date_input("请选择开始日期", value=current_date, 
                                      min_value=datetime.date(1989, 1, 1), 
                                      max_value=current_date)
        with col22:
            st.markdown("—", help="日期范围分隔符")
        with col23:
            end_date = st.date_input("请选择结束日期", value=current_date, 
                                    min_value=start_date, 
                                    max_value=current_date)
        
        # 处理数据
        monthly_avg = process_data(
            df, data_type, 
            pd.to_datetime(start_date), 
            pd.to_datetime(end_date),
            current_date
        )
    else:
        # 年统计数据界面
        current_year = current_date.year
        col21, col22, col23 = st.columns([1, 0.1, 1])
        with col21:
            start_year = st.selectbox("请选择起始年份", 
                                     list(range(1989, current_year + 1)), 
                                     index=0)
        with col22:
            st.markdown("—", help="年份范围分隔符")
        with col23:
            end_year = st.selectbox("请选择结束年份", 
                                   list(range(start_year, current_year + 1)), 
                                   index=current_year - start_year)
        
        # 处理数据
        monthly_avg = process_data(
            df, data_type, 
            datetime.date(start_year, 1, 1), 
            datetime.date(end_year, 12, 31),
            current_date
        )
    
    # 显示数据表格和图表
    display_data_table(monthly_avg)
    render_plots(monthly_avg)
    feature_plots(df)  # 显示特征指标