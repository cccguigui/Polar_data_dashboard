# -*- coding: utf-8 -*-
"""
图表渲染模块
功能：根据用户选择渲染不同类型的图表
Created on Fri Aug  8 13:55:16 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st
from utils.create_single_line_plot import create_single_line_plot
from utils.create_dual_axis_plot import create_dual_axis_plot

def render_plots(df):
    """
    渲染图表
    参数:
        df (DataFrame): 要可视化的数据框
    """
    with st.expander("查看折线图"):
        # 多选框选择变量
        choices = st.multiselect("请选择变量绘制折线图", options=df.columns)
        
        # 根据选择的数量创建不同类型的图表
        if len(choices) == 1:
            fig = create_single_line_plot(df, choices[0])
            st.plotly_chart(fig)
        elif len(choices) == 2:
            fig = create_dual_axis_plot(df, choices[0], choices[1])
            st.plotly_chart(fig)
        elif len(choices) > 2:
            st.info('最多支持两个变量绘制双轴折线图')