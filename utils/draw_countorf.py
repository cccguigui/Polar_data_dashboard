# -*- coding: utf-8 -*-
"""
等值线图绘制模块
功能：绘制极地气象要素的等值线分布图
Created on Fri Aug  8 15:35:08 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from utils.draw_map_base import draw_map_base
from utils.update_variable_field import update_variable_field

def draw_countourf(hemisphere):
    """
    绘制等值线分布图
    参数:
        hemisphere (str): 半球类型 ('南极' 或 '北极')
    """
    # 设置中文字体支持
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False    # 正常显示负号
    
    # 读取风温数据并转换为xarray格式
    file = pd.read_csv('./station/wind_temperature.csv').set_index(['lat','lon']).to_xarray()
    
    # 根据半球设置纬度范围
    if hemisphere == '南极':
        lat_slice = slice(-90, -60)
    else:
        lat_slice = slice(60, 90)
    
    # 创建可折叠容器
    with st.expander("查看温度/风速分布"):
        # 选择要查看的图形类型
        choice = st.selectbox("选择查看图形", 
                             options=['平均温度','最低温度','平均风速','最大风速'],
                             index=None)
        if choice == None:
            return
        # 根据选择配置数据参数
        elif choice == '平均温度':
            data = file['mean_skt'].sel(lat=lat_slice)
            vmin = -90
            vmax = 10
            interval = 10
            cmap=plt.cm.Blues_r  # 蓝色调色板（反转）
        elif choice == '最低温度':
            data = file['min_skt'].sel(lat=lat_slice)
            vmin = -90
            vmax = 10
            interval = 10
            cmap=plt.cm.Blues_r
        elif choice == '平均风速':
            data = file['mean_wind'].sel(lat=lat_slice)
            vmin = 0
            vmax = 50
            interval = 10
            cmap=plt.cm.Reds  # 红色调色板
        elif choice == '最大风速':
            data = file['max_wind'].sel(lat=lat_slice)
            vmin = 0
            vmax = 50
            interval = 10
            cmap=plt.cm.Reds
            
        # 绘制基础地图
        fig, ax = draw_map_base(hemisphere, f_color=True)
        title = hemisphere + choice + "分布图"
        
        # 更新变量场（绘制等值线）
        mesh, cbar = update_variable_field(
            ax=ax,
            data=data,
            cbar_label='Skin Temperature (°C)',
            hemisphere='south' if hemisphere == '南极' else 'north',
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            interval=interval,  # 10度间隔
            title=title
        )
        fig.tight_layout()
    
        # 在Streamlit中显示图形
        st.pyplot(fig)