# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:52:22 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

def process_data(df, data_type, start_date, end_date, current_date):
    if data_type == "月平均":
        monthly_avg = df[(df['时间'] >= start_date) & (df['时间'] <= end_date)]
        monthly_avg.set_index('时间', inplace=True)
        return monthly_avg
    else:
        df_filtered = df[(df['时间'].dt.year >= start_date.year) & 
                         (df['时间'].dt.year <= end_date.year)]
        if data_type == "年平均":
            monthly_avg = df_filtered.groupby(df_filtered["时间"].dt.year).mean()
            monthly_avg.index.name = '年份'
        elif data_type == "多年月平均":
            monthly_avg = df_filtered.groupby(df_filtered["时间"].dt.month).mean()
            monthly_avg.index.name = '月份'
        monthly_avg = monthly_avg.drop(columns=['时间'], errors='ignore')
        return monthly_avg