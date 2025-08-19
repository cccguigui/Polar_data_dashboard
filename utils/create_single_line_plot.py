# -*- coding: utf-8 -*-
"""
单线折线图创建模块
功能：创建单变量折线图
Created on Fri Aug  8 13:54:00 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import plotly.graph_objects as go

def create_single_line_plot(df, column):
    """
    创建单线折线图
    参数:
        df (DataFrame): 包含数据的数据框
        column (str): 要绘制的数据列名
    返回:
        Figure: Plotly图表对象
    """
    fig = go.Figure()
    # 添加折线轨迹
    fig.add_trace(go.Scatter(
        x=df.index, y=df[column], name=column, 
        mode='lines+markers', line=dict(color='black')
    ))
    # 更新布局
    fig.update_layout(
        xaxis_title=df.index.name,  # X轴标题
        yaxis_title=column,  # Y轴标题
        yaxis_dtick=5  # Y轴刻度间隔
    )
    return fig