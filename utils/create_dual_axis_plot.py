# -*- coding: utf-8 -*-
"""
双轴折线图创建模块
功能：创建带有双Y轴的折线图，用于比较两个不同量纲的变量
Created on Fri Aug  8 13:54:24 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

from plotly.subplots import make_subplots
import plotly.graph_objects as go

def create_dual_axis_plot(df, col1, col2):
    """
    创建双Y轴折线图
    参数:
        df (DataFrame): 包含数据的数据框
        col1 (str): 主Y轴数据列名
        col2 (str): 次Y轴数据列名
    返回:
        Figure: Plotly图表对象
    """
    # 创建带次Y轴的子图布局
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # 添加第一条折线（主Y轴）
    fig.add_trace(
        go.Scatter(x=df.index, y=df[col1], name=col1, 
                   mode='lines+markers', line=dict(color='blue')),
        secondary_y=False
    )
    
    # 添加第二条折线（次Y轴）
    fig.add_trace(
        go.Scatter(x=df.index, y=df[col2], name=col2, 
                   mode='lines+markers', line=dict(color='red')),
        secondary_y=True
    )
    
    # 更新图表布局
    fig.update_layout(
        xaxis_title=df.index.name,  # X轴标题
        yaxis=dict(  # 主Y轴配置
            title=col1,
            titlefont=dict(color="blue"),
            tickfont=dict(color="blue"),
            showgrid=True,
            gridcolor='lightgray',
            dtick=5  # 刻度间隔
        ),
        yaxis2=dict(  # 次Y轴配置
            title=col2,
            titlefont=dict(color="red"),
            tickfont=dict(color="red"),
            overlaying="y",  # 覆盖主Y轴
            side="right",  # 右侧显示
            showgrid=False,
            gridcolor='lightgray',
            dtick=5
        ),
        legend=dict(x=1.1, y=1.0),  # 图例位置
        margin=dict(r=200)  # 右边距
    )
    return fig