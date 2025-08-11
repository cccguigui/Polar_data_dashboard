# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:49:57 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import matplotlib.path as mpath

def draw_map_base(projection,f_color=False):
    fig = plt.figure(figsize=(10, 10))
    
    if projection == '南极':
        proj = ccrs.AzimuthalEquidistant(central_latitude=-90)
        ax = fig.add_subplot(111, projection=proj)
        ax.set_extent([-180, 180, -60, -90], crs=ccrs.PlateCarree())
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
    
    if f_color:
        ax.add_feature(cfeature.OCEAN, facecolor='white', zorder=0)
        ax.add_feature(cfeature.LAND, facecolor='none', edgecolor='k', linewidth=0.5, zorder=1)
        ax.add_feature(cfeature.LAKES, facecolor='none', edgecolor='k', linewidth=0.3, zorder=1)
        ax.add_feature(cfeature.RIVERS, edgecolor='k', linewidth=0.5, zorder=1)
        ax.add_feature(cfeature.COASTLINE, linewidth=0.8, zorder=1)
    else:
        ax.add_feature(cfeature.OCEAN)
        ax.add_feature(cfeature.LAND)
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.LAKES)
        ax.add_feature(cfeature.RIVERS)
    
    
    

    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)
    ax.set_boundary(circle, transform=ax.transAxes)

    return fig, ax