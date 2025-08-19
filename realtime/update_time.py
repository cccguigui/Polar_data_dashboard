# -*- coding: utf-8 -*-
"""
更新时间记录模块
功能：记录和获取数据最后更新时间
Created on Thu Aug 14 13:35:53 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
from datetime import datetime  # 日期时间处理
import os  # 操作系统接口

# 存储时间的文件路径
TIME_FILE = "./realtime/update_time.txt"

def get_last_update():
    """从文件获取上次更新时间"""
    if os.path.exists(TIME_FILE):
        with open(TIME_FILE, "r") as file:
            return file.read()
    return "尚未更新"  # 默认返回值

def save_last_update():
    """保存当前时间到文件"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 格式化当前时间
    with open(TIME_FILE, "w") as file:
        file.write(current_time)
    return current_time