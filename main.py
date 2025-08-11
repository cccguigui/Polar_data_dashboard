# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 14:04:53 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import datetime
from .polar_station_tab import polar_station_tab
from .company_station_tab import company_station_tab

def main():
    current_date = datetime.datetime.now()
    st.set_page_config(layout="wide")
    
    tab1, tab2 = st.tabs(["极地站点数据", "公司站点数据"])
    
    with tab1:
        polar_station_tab(current_date)
    
    with tab2:
        company_station_tab(current_date)

if __name__ == "__main__":
    main()
