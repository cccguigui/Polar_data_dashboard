# -*- coding: utf-8 -*-
"""
目录检查模块
功能：检查站点数据文件是否存在于指定目录
Created on Fri Aug  8 14:48:50 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import os

def is_in_dir(selected_station, station_dir):
    """
    检查站点数据文件是否存在
    参数:
        selected_station (str): 站点名称
        station_dir (str): 站点数据目录
    返回:
        bool: 文件是否存在
    """
    # 列出目录中所有文件（过滤掉子目录）
    filenames = [
        os.path.splitext(f)[0]  for f in os.listdir(station_dir)
        if os.path.isfile(os.path.join(station_dir, f))
    ]

    return selected_station in filenames