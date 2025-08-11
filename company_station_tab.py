# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 14:04:35 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st
import os
import datetime
import pandas as pd
from utils.process_company_data import process_company_data
from utils.display_data_table import display_data_table
from utils.render_plots import render_plots

def company_station_tab(current_date: datetime.datetime):
    st.title("公司极地数据看板")
    path = './station/公司站点数据'
    option = st.radio("选择数据类型：", os.listdir(path), horizontal=True)
    
    data_type = st.selectbox("请选择时间粒度", ("逐小时数据", "月平均"), index=0)
    df, start_time, end_time = process_company_data(option)
    
    col21, col22, col23 = st.columns([1, 0.1, 1])
    with col21:
        start_date = st.date_input("请选择开始日期", value=start_time, 
                                  min_value=start_time, 
                                  max_value=end_time)
    with col22:
        st.markdown("—", help="日期范围分隔符")
    with col23:
        end_date = st.date_input("请选择结束日期", value=end_time, 
                                min_value=start_date, 
                                max_value=end_time)
    
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    filtered_df = df[(df['观测时间'] >= start_date) & (df['观测时间'] <= end_date)]
    
    if data_type == "月平均":
        monthly_avg = filtered_df.groupby([filtered_df["观测时间"].dt.year, 
                                          filtered_df["观测时间"].dt.month]).mean()
        monthly_avg.index.names = ['年份', '月份']
        monthly_avg = monthly_avg.drop(columns=['观测时间', "到报时间"], errors='ignore')
        monthly_avg['日期'] = pd.to_datetime(
            monthly_avg.index.get_level_values('年份').astype(str) + '-' +
            monthly_avg.index.get_level_values('月份').astype(str) + '-01'
        )
        monthly_avg = monthly_avg.set_index('日期')
        monthly_avg.index = monthly_avg.index.strftime('%Y-%m')
    else:
        filtered_df.set_index('观测时间', inplace=True)
        monthly_avg = filtered_df
    
    display_data_table(monthly_avg)
    render_plots(monthly_avg)