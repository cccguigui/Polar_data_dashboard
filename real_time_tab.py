# -*- coding: utf-8 -*-
"""
实时数据看板模块
功能：展示实时气象数据和提供数据更新功能
Created on Tue Aug 12 16:13:55 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st  # Web应用框架
from realtime.update_realtime_station import update_realtime_station  # 实时数据更新
import streamlit.components.v1 as components  # 自定义组件支持
from realtime.update_time import get_last_update, save_last_update  # 更新时间记录
from realtime.display_data_table import display_data_table  # 数据展示

def real_time_tab():
    """实时数据看板标签页"""
    # 实时数据网站嵌入
    st.title('实时小时数据')
    with st.expander('实时数据网站'):
        st.link_button("点击进入网站", "http://meteo.hbaa.cn/src/")
        # 嵌入外部网站
        components.iframe("http://meteo.hbaa.cn/src/", height=500, scrolling=True)
    
    # 实时周数据展示
    st.divider()
    st.header('实时周数据')
    display_data_table()  # 展示现有数据
    
    # 创建更新时间显示区域
    col1, col2 = st.columns([1, 1])
    with col1:
        time_display = st.empty()  # 创建占位符用于动态更新
    with col2:
        st.write('数据来源：https://pole.whu.edu.cn/cn/gb_news.php?modid=02001')
    
    # 显示上次更新时间
    time_display.write('上次更新时间：' + get_last_update())
    
    # 创建操作按钮区域
    col1, col2, col3, col_empty = st.columns([3, 4, 4, 20])
    with col1:
        # 更新数据按钮
        if st.button('更新周数据'):
            time_display.write('上次更新时间：' + save_last_update())
            update_realtime_station()
    with col2:
        # CSV下载按钮
        file_path = './station/极地周气象数据/极地气象数据.csv'
        with open(file_path, 'rb') as f:
            st.download_button(
                label='极地气象数据.csv',
                data=f,
                file_name="极地气象数据.csv",
                mime="text/csv",
                icon=":material/download:"
            )
    with col3:
        # Excel下载按钮
        file_path = './station/极地周气象数据/极地气象数据.xlsx'
        with open(file_path, 'rb') as f:
            st.download_button(
                label='极地气象数据.xlsx',
                data=f,
                file_name="极地气象数据.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                icon=":material/download:"
            )
    
    return