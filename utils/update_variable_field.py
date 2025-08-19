# -*- coding: utf-8 -*-
"""
变量场更新模块
功能：在地图上绘制气象变量分布
Created on Fri Aug  8 15:30:33 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np
import xarray as xr
import matplotlib.colors as colors
from utils.load_station_data import load_station_data

def update_variable_field(ax, data, title=None, cbar_label=None, hemisphere='北极', 
                          cmap=plt.cm.coolwarm_r, vmin=-40, vmax=20, interval=10):
    """
    更新变量场（绘制等值线）
    参数:
        ax (Axes): Matplotlib坐标轴对象
        data (DataArray): 要绘制的数据
        title (str): 图表标题
        cbar_label (str): 色标标签
        hemisphere (str): 半球 ('南极' 或 '北极')
        cmap: 颜色映射
        vmin: 最小值
        vmax: 最大值
        interval: 等值线间隔
    返回:
        tuple: (等值线对象, 色标对象)
    """
    # 确保经度连续性
    if data.lon.max() < 360:
        data = xr.concat([data, data.sel(lon=0).assign_coords(lon=360)], dim='lon')
    
    # 创建等值线级别
    levels = np.arange(vmin, vmax + interval, interval)
    
    # 创建离散颜色映射
    norm = colors.BoundaryNorm(boundaries=levels, ncolors=cmap.N)
    
    # 绘制填充等值线
    mesh = data.plot.contourf(
        ax=ax,
        transform=ccrs.PlateCarree(),  # 数据坐标系统
        cmap=cmap,
        norm=norm,
        levels=levels,
        add_colorbar=False,  # 稍后手动添加色标
        zorder=0,
        extend='both'  # 扩展颜色范围
    )
    
    # 绘制等值线标签
    c_label = data.plot.contour(
        ax=ax,
        transform=ccrs.PlateCarree(),
        levels=levels, 
        colors='black',  # 标签颜色
        linewidths=0,
        zorder=1,
    )
    ax.clabel(c_label, inline=True, fontsize=10, fmt='%1.1f', zorder=1, rightside_up=True) 
    
    # 添加色标
    cbar = plt.colorbar(mesh, ax=ax, orientation='vertical', pad=0.05, fraction=0.05)
    cbar.set_label(cbar_label, fontsize=12)
    cbar.set_ticks(levels)  # 设置色标刻度
    
    # 添加标题
    plt.title(title, fontsize=16, pad=20)
    
    # 标记重要站点（南极）
    if hemisphere == '南极':
        # 中国站点（红色）
        stations = [
             {'station': '长城站', 'longitude': -58.98, 'latitude': -62.22},
            {'station': '中山站', 'longitude': 76.37, 'latitude': -69.37},
            {'station': '昆仑站', 'longitude': 77.12, 'latitude': -80.42},
            {'station': '泰山站', 'longitude': 76.97, 'latitude': -73.85},
            {'station': '秦岭站', 'longitude': 163.70, 'latitude': -74.93},
        ]
        for station in stations:
            ax.plot(station['longitude'], station['latitude'], 'ro', markersize=8, 
                    transform=ccrs.PlateCarree(), zorder=2)
            ax.text(station['longitude'] + 1.5, station['latitude'] + 1.5, station['station'], 
                    fontsize=7, weight='bold', color='red',
                    transform=ccrs.PlateCarree(), zorder=2)
        
        # 其他国家站点（绿色）
        stations = [
            {"station": "奥卡达斯基地 ", "latitude": -60.73, "longitude": -44.73},
            {"station": "麦克默多站", "latitude": -77.83, "longitude": 166.67},
            {"station": "东方站", "latitude": -78.45, "longitude": 106.87},
            {"station": "阿蒙森-斯科特站", "latitude": -90, "longitude": 0},
            {"station": "康宏站", "latitude": -75.1, "longitude": 123.33},
            {"station": "富士冰穹站", "latitude": -77.32, "longitude": 39.70},
        ]
        for station in stations:
            ax.plot(station['longitude'], station['latitude'], 'go', markersize=8, 
                    transform=ccrs.PlateCarree(), zorder=2)
            ax.text(station['longitude'] + 1.5, station['latitude'] + 1.5, station['station'], 
                    fontsize=7, weight='bold', color='green',
                    transform=ccrs.PlateCarree(), zorder=2)
    
    # 标记重要站点（北极）
    elif hemisphere == '北极':
        # 中国站点（红色）
        stations = [
             {'station': '黄河站', 'longitude': 11.93, 'latitude': 78.92},
            {'station': '中-冰北极科考站', 'longitude': -17.36, 'latitude': 65.71},
        ]
        for station in stations:
            ax.plot(station['longitude'], station['latitude'], 'ro', markersize=8, 
                    transform=ccrs.PlateCarree(), zorder=2)
            ax.text(station['longitude'] + 1.5, station['latitude'] + 1.5, station['station'], 
                    fontsize=7, weight='bold', color='red',
                    transform=ccrs.PlateCarree(), zorder=2)
    
    # 加载并标记所有站点（橙色）
    df = load_station_data(hemisphere)
    df = df[['Name', 'Latitude', 'Longitude', 'Party']].dropna()
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)
    for _, row in df.iterrows():
        ax.plot(row['Longitude'], row['Latitude'], marker='o', color='orange', markersize=4,
                transform=ccrs.PlateCarree(), zorder=1)
        
    return mesh, cbar