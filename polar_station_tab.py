# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:55:33 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st
import datetime
from utils.load_station_data import load_station_data
from utils.draw_map_base import draw_map_base
from utils.update_station_points import update_station_points
from utils.render_data import render_data
from utils.is_in_dir import is_in_dir
from utils.draw_countorf import draw_countourf

def polar_station_tab(current_date: datetime.datetime):
    st.title("极地数据看板")
    df = load_station_data()
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("🎯 站点选择与详情")
        projection_option = st.selectbox("请选择地图区域", ("南极", "北极"))
        draw_countourf(projection_option)
        fig, ax = draw_map_base(projection=projection_option)
        
        if projection_option == '南极':
            countries = df['Party'].unique().tolist()
            selected_country = st.selectbox("请选择一个国家", countries, index=7)
            filtered_df = df[df['Party'] == selected_country]
        else:
            filtered_df = df
            
        station_names = filtered_df['Name'].tolist()
        selected_station = st.selectbox("请选择一个站点", station_names, index=2)
        
        if selected_station:
            station_row = filtered_df[filtered_df['Name'] == selected_station].iloc[0]
            col11, col12 = st.columns([1, 1])
            with col11:
                st.markdown(f"- **名称**：{station_row['Name']}")
                st.markdown(f"- **纬度**：{station_row['Latitude']}°")
            with col12:
                st.markdown(f"- **国家**：{station_row['Party']}")
                st.markdown(f"- **经度**：{station_row['Longitude']}°")
        
        update_station_points(ax, df, selected_station=selected_station)
        st.pyplot(fig)
    
    with col2:
        st.subheader("📊 站点数据图")
        if is_in_dir(selected_station, './station'):
            render_data(selected_station,current_date)
        else:
            st.info("当前站点无数据")