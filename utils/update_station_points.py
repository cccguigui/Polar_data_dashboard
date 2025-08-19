# -*- coding: utf-8 -*-
"""
站点标记更新模块
功能：在地图上标记站点位置
Created on Fri Aug  8 13:51:29 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import cartopy.crs as ccrs

def update_station_points(ax, df, selected_station=None):
    """
    在地图上标记站点位置
    参数:
        ax (Axes): Matplotlib坐标轴对象
        df (DataFrame): 站点数据框
        selected_station (str): 选中的站点名称
    """
    # 标记所有站点
    for _, row in df.iterrows():
        ax.plot(row['Longitude'], row['Latitude'], marker='o', 
                color='red', markersize=4, transform=ccrs.PlateCarree())
    
    # 高亮标记选中的站点
    if selected_station:
        station_row = df[df['Name'] == selected_station].iloc[0]
        ax.plot(station_row['Longitude'], station_row['Latitude'], 
                marker='o', color='blue', markersize=8, transform=ccrs.PlateCarree())
        # 添加站点名称标签
        ax.text(station_row['Longitude'] + 1, station_row['Latitude'] + 1, 
                selected_station, fontsize=9, color='blue', 
                transform=ccrs.PlateCarree())