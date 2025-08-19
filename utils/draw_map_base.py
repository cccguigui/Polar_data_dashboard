# -*- coding: utf-8 -*-
"""
基础地图绘制模块
功能：创建极地地区的基础地图
Created on Fri Aug  8 13:49:57 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import matplotlib.path as mpath

def draw_map_base(projection, f_color=False):
    """
    绘制基础极地地图
    参数:
        projection (str): 投影类型 ('南极' 或 '北极')
        f_color (bool): 是否使用简化着色
    返回:
        Figure: Matplotlib图形对象
        Axes: Matplotlib坐标轴对象
    """
    fig = plt.figure(figsize=(10, 10))
    
    # 根据投影类型设置坐标系
    if projection == '南极':
        proj = ccrs.AzimuthalEquidistant(central_latitude=-90)
        ax = fig.add_subplot(111, projection=proj)
        ax.set_extent([-180, 180, -60, -90], crs=ccrs.PlateCarree())
        # 添加网格线
        ax.gridlines(draw_labels=True, crs=ccrs.PlateCarree(), 
                           color='k', linestyle='dashed', linewidth=0.3, 
                           dms=True, x_inline=False, y_inline=True,
                           xlocs=np.arange(-180, 180 + 60, 60), 
                           ylocs=np.arange(-90+10, -60, 10))
    else:
        proj = ccrs.AzimuthalEquidistant(central_latitude=90)
        ax = fig.add_subplot(111, projection=proj)
        ax.set_extent([-180, 180, 60, 90], crs=ccrs.PlateCarree())
        ax.gridlines(draw_labels=True, crs=ccrs.PlateCarree(), 
                           color='k', linestyle='dashed', linewidth=0.3, 
                           dms=True, x_inline=False, y_inline=True,
                           xlocs=np.arange(-180, 180 + 60, 60), 
                           ylocs=np.arange(60+10, 90, 10))
    
    # 添加地理特征
    if f_color:
        # 简化着色模式
        ax.add_feature(cfeature.OCEAN, facecolor='white', zorder=0)
        ax.add_feature(cfeature.LAND, facecolor='none', edgecolor='k', linewidth=0.5, zorder=1)
        ax.add_feature(cfeature.LAKES, facecolor='none', edgecolor='k', linewidth=0.3, zorder=1)
        ax.add_feature(cfeature.RIVERS, edgecolor='k', linewidth=0.5, zorder=1)
        ax.add_feature(cfeature.COASTLINE, linewidth=0.8, zorder=1)
    else:
        # 标准着色模式
        ax.add_feature(cfeature.OCEAN)
        ax.add_feature(cfeature.LAND)
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.LAKES)
        ax.add_feature(cfeature.RIVERS)
    
    # 创建圆形边界
    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)
    ax.set_boundary(circle, transform=ax.transAxes)

    return fig, ax