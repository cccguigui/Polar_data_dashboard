# -*- coding: utf-8 -*-
"""
极地站点数据看板模块
功能：展示极地站点地图和数据可视化
Created on Fri Aug  8 13:55:33 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st  # Web应用框架
import datetime  # 日期时间处理
import pandas as pd
from utils.load_station_data import load_station_data  # 站点数据加载工具
from utils.draw_map_base import draw_map_base  # 基础地图绘制工具
from utils.update_station_points import update_station_points  # 站点标记工具
from utils.render_data import render_data  # 数据渲染工具
from utils.is_in_dir import is_in_dir  # 目录检查工具
from utils.draw_countorf import draw_countourf  # 等值线图工具
from utils.upload_files import upload_files  # 文件上传工具

def polar_station_tab(current_date: datetime.datetime):
    """
    极地站点数据看板标签页
    参数:
        current_date (datetime): 当前日期时间
    """
    # 创建标题和上传按钮
    col, col_file = st.columns([10, 1])
    with col:
        st.title("极地数据看板")
    with col_file:
        if st.button('upload files'):
            upload_files()  # 打开文件上传对话框
        
    # 创建两列布局
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎯 站点选择与详情")
        
        # 选择地图区域
        projection_option = st.selectbox("请选择地图区域", ("南极", "北极"))
        
        # 绘制等值线图
        draw_countourf(projection_option)
        
        # 绘制基础地图
        fig, ax = draw_map_base(projection=projection_option)
        
        # 加载站点数据
        df = load_station_data(projection_option)

        # 国家选择器
        countries = df['Party'].unique().tolist()
        selected_country = st.selectbox("请选择一个国家", countries, index=None)
        
        # 根据国家过滤站点
        if selected_country:
            filtered_df = df[df['Party'] == selected_country]
        else:
            filtered_df = pd.DataFrame()
        
        # 站点选择器
        station_names = filtered_df['Name'].tolist() if not filtered_df.empty else []
        selected_station = st.selectbox("请选择一个站点", station_names, index=None)
        
        # 显示站点详情
        if selected_station:
            station_row = filtered_df[filtered_df['Name'] == selected_station].iloc[0]
            col11, col12 = st.columns([1, 1])
            with col11:
                st.markdown(f"- **名称**：{station_row['Name']}")
                st.markdown(f"- **纬度**：{station_row['Latitude']:.2f}°")
            with col12:
                st.markdown(f"- **国家**：{station_row['Party']}")
                st.markdown(f"- **经度**：{station_row['Longitude']:.2f}°")
        
        # 在地图上标记站点
        update_station_points(ax, df, selected_station=selected_station)
        st.pyplot(fig)  # 显示地图
    
    with col2:
        st.subheader("📊 站点数据图")
        # 检查站点是否有数据并渲染
        if selected_station and is_in_dir(selected_station, './station'):
            render_data(selected_station, current_date)
        else:
            st.info("当前站点无数据")