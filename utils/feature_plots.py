# -*- coding: utf-8 -*-
"""
气象特征可视化模块
功能：展示温压湿风等关键气象指标
Created on Wed Aug 13 10:56:58 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import streamlit as st
import pandas as pd

def get_stat(data, col_priority, stat_func, default="暂无该数据", format_str="{:.2f}"):
    """
    通用方法获取统计数据
    参数:
        data (DataFrame): 输入数据集
        col_priority (list): 列名优先级列表
        stat_func (function): 统计函数（如min, max, mean）
        default (str): 默认返回值
        format_str (str): 数值格式化字符串
    返回:
        str: 格式化后的统计结果
    """
    # 按优先级查找可用的列
    for col in col_priority:
        if col in data.columns:
            value = stat_func(data[col])  # 应用统计函数
            # 检查结果是否为有效数值
            if pd.notna(value) and value != "":
                return format_str.format(value)
    return default

def feature_plots(data):
    """
    展示温压湿风等关键气象指标
    参数:
        data (DataFrame): 包含气象数据的数据集
    """
    # 创建4列布局
    a, b, c, d = st.columns(4)
    
    # 温度指标计算
    temp_avg = get_stat(data, ['平均温度','温度'], pd.Series.mean, format_str="{:.2f} °C")
    temp_min = get_stat(
        data, 
        ['最低温度', '平均温度','温度'],  # 列名优先级
        pd.Series.min, 
        default="", 
        format_str="{:.2f} °C(min)"
    )
    
    # 风速指标计算
    wind_avg = get_stat(data, ['平均风速','风速'], pd.Series.mean, format_str="{:.2f} m/s")
    wind_max = get_stat(
        data, 
        ['极大风速', '最大风速', '平均风速','风速'],  
        pd.Series.max, 
        default="", 
        format_str="{:.2f} m/s(max)"
    )
    
    # 湿度指标计算
    hum_avg = get_stat(data, ['平均湿度','湿度'], pd.Series.mean, format_str="{:.2f} %")
    hum_min = get_stat(
        data, 
        ['最小湿度', '平均湿度','湿度'], 
        pd.Series.min, 
        default=" ", 
        format_str="{:.2f} %(min)"
    )
    
    # 气压指标计算
    pres_avg = get_stat(data, ['平均气压','气压'], pd.Series.mean, format_str="{:.2f} hPa")
    pres_min = get_stat(
        data, 
        ['最低气压', '平均气压','气压'], 
        pd.Series.min, 
        default=" ", 
        format_str="{:.2f} hPa(min)"
    )
    
    # 使用metric组件展示结果
    a.metric("温度", temp_avg, temp_min, border=True)
    b.metric("风速", wind_avg, wind_max, border=True)
    c.metric("湿度", hum_avg, hum_min, border=True)
    d.metric("气压", pres_avg, pres_min, border=True)