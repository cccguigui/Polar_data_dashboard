# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:54:24 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

from plotly.subplots import make_subplots
import plotly.graph_objects as go

def create_dual_axis_plot(df, col1, col2):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(x=df.index, y=df[col1], name=col1, 
                   mode='lines+markers', line=dict(color='blue')),
        secondary_y=False
    )
    
    fig.add_trace(
        go.Scatter(x=df.index, y=df[col2], name=col2, 
                   mode='lines+markers', line=dict(color='red')),
        secondary_y=True
    )
    
    fig.update_layout(
        xaxis_title=df.index.name,
        yaxis=dict(
            title=col1,
            titlefont=dict(color="blue"),
            tickfont=dict(color="blue"),
            showgrid=True,
            gridcolor='lightgray',
            dtick=5
        ),
        yaxis2=dict(
            title=col2,
            titlefont=dict(color="red"),
            tickfont=dict(color="red"),
            overlaying="y",
            side="right",
            showgrid=False,
            gridcolor='lightgray',
            dtick=5
        ),
        legend=dict(x=1.1, y=1.0),
        margin=dict(r=200)
    )
    return fig