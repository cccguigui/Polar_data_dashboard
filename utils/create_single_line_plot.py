# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:54:00 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import plotly.graph_objects as go

def create_single_line_plot(df, column):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df.index, y=df[column], name=column, 
        mode='lines+markers', line=dict(color='black')
    ))
    fig.update_layout(
        xaxis_title=df.index.name,
        yaxis_title=column,
        yaxis_dtick=5
    )
    return fig