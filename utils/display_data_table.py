# -*- coding: utf-8 -*-
"""
数据表格展示模块
功能：提供交互式数据表格展示功能
Created on Fri Aug  8 13:54:25 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st

def display_data_table(df):
    """
    展示交互式数据表格
    参数:
        df (DataFrame): 要展示的数据框
    """
    # 创建多选框选择要显示的列
    choice = st.multiselect("请选择需要查看的数据", 
                           options=["全选"] + list(df.columns))
    
    # 根据选择展示数据
    if "全选" in choice or not choice:
        st.dataframe(df, height=300)  # 显示完整数据框
    else:
        st.dataframe(df[choice], height=300)  # 显示选定列