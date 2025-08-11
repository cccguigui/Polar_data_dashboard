# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:54:25 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st

def display_data_table(df):
    choice = st.multiselect("请选择需要查看的数据", 
                           options=["全选"] + list(df.columns))
    
    if "全选" in choice or not choice:
        st.dataframe(df, height=300)
    else:
        st.dataframe(df[choice], height=300)