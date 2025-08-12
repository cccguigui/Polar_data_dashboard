# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 15:35:08 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import streamlit as st
import matplotlib.pyplot as plt
import xarray as xr
from utils.draw_map_base import draw_map_base
from utils.update_variable_field import update_variable_field

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

def  draw_countourf(hemisphere):
    file = xr.open_mfdataset(r".\station\wind_temperature.nc")
    if hemisphere == '南极':
        lat_slice = slice(-90, -60)
    else:
        lat_slice = slice(60, 90)
    
    with st.expander("查看温度/风速分布"):
        choice = st.selectbox("选择查看图形", options=['平均温度','最低温度','平均风速','最大风速'],index=None)
        print(choice)
        if choice == None:
            return
        elif choice == '平均温度':
            data = file['mean_skt'].sel(lat=lat_slice)
            vmin = -90
            vmax = 10
            interval = 10
            cmap=plt.cm.Blues_r
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
            cmap=plt.cm.Reds
        elif choice == '最大风速':
            data = file['max_wind'].sel(lat=lat_slice)
            vmin = 0
            vmax = 50
            interval = 10
            cmap=plt.cm.Reds
            
        fig, ax = draw_map_base(hemisphere,f_color = True)
        title=hemisphere+choice+"分布图"
        mesh, cbar = update_variable_field(
            ax=ax,
            data=data,
            cbar_label='Skin Temperature (°C)',
            hemisphere='south',
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            interval=interval,  # 10度间隔
            title=title
        )
        fig.tight_layout()
        st.pyplot(fig)

    
    
    