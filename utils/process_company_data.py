# -*- coding: utf-8 -*-
"""
公司数据处理模块
功能：处理公司提供的站点数据
Created on Fri Aug  8 13:52:20 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import pandas as pd
import glob

def process_company_data(option):
    """
    处理公司提供的站点数据
    参数:
        option (str): 数据类型选项
    返回:
        tuple: (处理后的数据框, 最新时间, 最早时间)
    """
    # 根据选项选择文件路径
    if option == "北极浮标数据":
        excel_path = "./station/公司站点数据/北极浮标数据/*.xlsx"
        df = pd.concat([pd.read_excel(f, engine='openpyxl') for f in glob.glob(excel_path)])
        df = df.drop(df.columns[0], axis=1)  # 删除第一列
    else:
        excel_path = f"./station/公司站点数据/{option}/*.csv"
        df = pd.concat([pd.read_csv(f) for f in glob.glob(excel_path)])
    
    # 时间处理
    df['观测时间'] = pd.to_datetime(df['观测时间'])
    
    if '到报时间' in df.columns:
        df['到报时间'] = pd.to_datetime(df['到报时间'])
    
    # 返回处理后的数据和时间范围
    return df, df['观测时间'].iloc[-1], df['观测时间'].iloc[0]