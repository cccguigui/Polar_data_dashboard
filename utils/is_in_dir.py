# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 14:48:50 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import os

def is_in_dir(selected_station,station_dir):

    # 列出所有文件（过滤掉子目录）
    filenames = [
        os.path.splitext(f)[0]  for f in os.listdir(station_dir)
        if os.path.isfile(os.path.join(station_dir, f))
    ]

    return selected_station in filenames

    