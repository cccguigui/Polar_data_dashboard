# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:52:20 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import pandas as pd

def process_company_data(option):
    path = './station/公司站点数据'
    if option == "北极浮标数据":
        excel_path = "./station/公司站点数据/北极浮标数据/24年北极浮标.xlsx"
        df = pd.read_excel(excel_path, engine='openpyxl')
        df = df.drop(df.columns[0], axis=1)
    else:
        excel_path = f"./station/公司站点数据/{option}/query_1.csv"
        df = pd.read_csv(excel_path)
    
    df['观测时间'] = pd.to_datetime(df['观测时间'])
    
    if '到报时间' in df.columns:
        df['到报时间'] = pd.to_datetime(df['到报时间'])
    
    return df, df['观测时间'].iloc[-1], df['观测时间'].iloc[0]