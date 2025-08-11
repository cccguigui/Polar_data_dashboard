# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:51:29 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import cartopy.crs as ccrs

def update_station_points(ax, df, selected_station=None):
    for _, row in df.iterrows():
        ax.plot(row['Longitude'], row['Latitude'], marker='o', 
                color='red', markersize=4, transform=ccrs.PlateCarree())
    
    if selected_station:
        station_row = df[df['Name'] == selected_station].iloc[0]
        ax.plot(station_row['Longitude'], station_row['Latitude'], 
                marker='o', color='blue', markersize=8, transform=ccrs.PlateCarree())
        ax.text(station_row['Longitude'] + 1, station_row['Latitude'] + 1, 
                selected_station, fontsize=9, color='blue', 
                transform=ccrs.PlateCarree())