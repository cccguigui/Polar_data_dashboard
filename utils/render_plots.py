# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:55:16 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import streamlit as st
from utils.create_single_line_plot import create_single_line_plot
from utils.create_dual_axis_plot import create_dual_axis_plot

def render_plots(df):
    with st.expander("查看折线图"):
        choices = st.multiselect("请选择变量绘制折线图", options=df.columns)
        
        if len(choices) == 1:
            fig = create_single_line_plot(df, choices[0])
            st.plotly_chart(fig)
        elif len(choices) == 2:
            fig = create_dual_axis_plot(df, choices[0], choices[1])
            st.plotly_chart(fig)