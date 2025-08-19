# -*- coding: utf-8 -*-
"""
数据处理模块
功能：根据不同类型处理气象数据
Created on Fri Aug  8 13:52:22 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

def process_data(df, data_type, start_date, end_date, current_date):
    """
    处理气象数据
    参数:
        df (DataFrame): 原始数据框
        data_type (str): 数据类型 ('月平均', '年平均', '多年月平均')
        start_date (datetime): 开始日期
        end_date (datetime): 结束日期
        current_date (datetime): 当前日期
    返回:
        DataFrame: 处理后的数据
    """
    if data_type == "月平均":
        # 月平均数据处理
        monthly_avg = df[(df['时间'] >= start_date) & (df['时间'] <= end_date)]
        monthly_avg.set_index('时间', inplace=True)
        return monthly_avg
    else:
        # 按年过滤数据
        df_filtered = df[(df['时间'].dt.year >= start_date.year) & 
                         (df['时间'].dt.year <= end_date.year)]
        
        if data_type == "年平均":
            # 计算年平均
            monthly_avg = df_filtered.groupby(df_filtered["时间"].dt.year).mean()
            monthly_avg.index.name = '年份'
        elif data_type == "多年月平均":
            # 计算多年月平均
            monthly_avg = df_filtered.groupby(df_filtered["时间"].dt.month).mean()
            monthly_avg.index.name = '月份'
        
        # 删除时间列（如果存在）
        monthly_avg = monthly_avg.drop(columns=['时间'], errors='ignore')
        return monthly_avg