# -*- coding: utf-8 -*-
"""
主程序入口模块
功能：创建应用主框架和标签页导航
Created on Fri Aug  8 14:04:53 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st  # Web应用框架
import datetime  # 日期时间处理
from polar_station_tab import polar_station_tab  # 极地站点标签页
from company_station_tab import company_station_tab  # 公司站点标签页
from real_time_tab import real_time_tab  # 实时数据标签页

def main():
    """主函数，配置页面并组织标签页"""
    current_date = datetime.datetime.now()
    st.set_page_config(layout="wide")  # 设置宽屏布局
    
    # 创建标签页
    tab1, tab2, tab3 = st.tabs(["极地站点数据", "公司站点数据", "实时数据"])
    
    with tab1:
        polar_station_tab(current_date)  # 极地站点数据标签页
    
    with tab2:
        company_station_tab(current_date)  # 公司站点数据标签页
        
    with tab3:
        real_time_tab()  # 实时数据标签页

if __name__ == "__main__":
    main()  # 启动应用