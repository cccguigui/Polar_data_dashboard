# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 14:04:17 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st
import datetime
import pandas as pd
from utils.process_data import process_data
from utils.display_data_table import display_data_table
from utils.render_plots import render_plots

def render_data(selected_station,current_date: datetime.datetime):
    data_type = st.selectbox("请选择查看数据类型", ("多年月平均", "年平均", "月平均"), index=0)
    excel_path = "./station/"+selected_station+".xlsx"
    df = pd.read_excel(excel_path, engine='openpyxl')
    
    if data_type == "月平均":
        col21, col22, col23 = st.columns([1, 0.1, 1])
        with col21:
            start_date = st.date_input("请选择开始日期", value=current_date, 
                                      min_value=datetime.date(1989, 1, 1), 
                                      max_value=current_date)
        with col22:
            st.markdown("—", help="日期范围分隔符")
        with col23:
            end_date = st.date_input("请选择结束日期", value=current_date, 
                                    min_value=start_date, 
                                    max_value=current_date)
        
        monthly_avg = process_data(
            df, data_type, 
            pd.to_datetime(start_date), 
            pd.to_datetime(end_date),
            current_date
        )
    else:
        current_year = current_date.year
        col21, col22, col23 = st.columns([1, 0.1, 1])
        with col21:
            start_year = st.selectbox("请选择起始年份", 
                                     list(range(1989, current_year + 1)), 
                                     index=0)
        with col22:
            st.markdown("—", help="年份范围分隔符")
        with col23:
            end_year = st.selectbox("请选择结束年份", 
                                   list(range(start_year, current_year + 1)), 
                                   index=current_year - start_year)
        
        monthly_avg = process_data(
            df, data_type, 
            datetime.date(start_year, 1, 1), 
            datetime.date(end_year, 12, 31),
            current_date
        )
    
    display_data_table(monthly_avg)
    render_plots(monthly_avg)