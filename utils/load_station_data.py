# -*- coding: utf-8 -*-
"""
站点数据加载模块
功能：加载南极或北极站点数据
Created on Fri Aug  8 13:51:46 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import pandas as pd
import streamlit as st

@st.cache_data  # Streamlit数据缓存装饰器
def load_station_data(permission):
    """
    加载站点数据
    参数:
        permission (str): 区域权限 ('南极' 或 '北极')
    返回:
        DataFrame: 站点数据框
    """
    # 根据区域选择数据文件
    if permission == '南极':
        url = "./station/Antarctic.csv"
    else:
        url = "./station/Arctic.csv"
    
    # 读取数据并处理
    df = pd.read_csv(url)
    df = df[['Name', 'Latitude', 'Longitude', 'Party']].dropna()
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)
    return df