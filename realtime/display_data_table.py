# -*- coding: utf-8 -*-
"""
极地气象数据展示模块
功能：读取Excel数据，提供交互式表格展示和关键指标可视化
Created on Fri Aug 15 10:41:59 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import streamlit as st  # 用于构建Web应用
import pandas as pd  # 数据处理库
import numpy as np  # 数值计算库

def display_data_table():
    """展示极地气象数据表格和关键指标"""
    file_path = './station/极地周气象数据/极地气象数据.xlsx'
    # 读取Excel文件，sheet_name=None表示读取所有sheet
    all_sheets = pd.read_excel(file_path, sheet_name=None)
    
    # 提取sheet名称列表并创建分段控制器
    sheet_names = list(all_sheets.keys())
    selection = st.segmented_control(
        "", sheet_names, selection_mode="single"
    )
    
    if selection:
        # 获取选中的sheet数据
        file = all_sheets.get(selection)
        file = file.drop(file.columns[0], axis=1)  # 删除第一列（通常是索引列）
        
        # 提取数字列用于高亮显示
        numeric_cols = file.select_dtypes(include=np.number).columns.tolist()
        
        # 展示交互式数据表格（带高亮效果）
        st.dataframe(file.style
                     .highlight_min(subset=numeric_cols, axis=0, props='background-color: blue; color: white;')  # 最小值蓝色高亮
                     .highlight_max(subset=numeric_cols, axis=0, props='background-color: red; color: white;'),  # 最大值红色高亮
                     column_config={
                         "周报URL": st.column_config.LinkColumn(  # 配置URL列为可点击链接
                             "周报链接", display_text="Open URL"
                         ),
                     },
                     hide_index=True)  # 隐藏默认索引
        
        # 创建统计行（最大值、最小值、平均值）
        stats_df = pd.DataFrame({
            '统计类型': ['最大值', '最小值', '平均值']
        })
        
        # 为每个数字列添加统计值
        for col in numeric_cols:
            stats_df[col] = [
                file[col].max(),
                file[col].min(),
                file[col].mean()
            ]
        
        # 展示统计表格
        st.dataframe(stats_df, hide_index=True)
        
        # 创建6列布局用于展示关键指标
        a, b, c, d, e, f = st.columns(6)
        
        # 温度指标（当前值及变化量）
        a.metric("本周温度", 
                 f"{file['温度(℃)'].iloc[-1]:.2f} °C", 
                 f"{file['温度(℃)'].iloc[-1]-file['温度(℃)'].iloc[-2]:+.2f} °C", 
                 border=True)
        
        # 风速指标
        b.metric("本周风速", 
                 f"{file['风速(m/s)'].iloc[-1]:.2f} m/s", 
                 f"{file['风速(m/s)'].iloc[-1] - file['风速(m/s)'].iloc[-2]:+.2f} m/s", 
                 border=True)
        
        # 湿度指标
        c.metric("本周湿度", 
                 f"{file['湿度(%)'].iloc[-1]:.1f} %", 
                 f"{file['湿度(%)'].iloc[-1] - file['湿度(%)'].iloc[-2]:+.1f} %", 
                 border=True)
        
        # 气压指标
        d.metric("本周气压", 
                 f"{file['气压(mb)'].iloc[-1]:.1f} mb", 
                 f"{file['气压(mb)'].iloc[-1] - file['气压(mb)'].iloc[-2]:+.1f} mb", 
                 border=True)
        
        # 周温差指标
        e.metric("本周温差", 
                 f"{file['周温差(℃)'].iloc[-1]:.2f} °C", 
                 f"{file['周温差(℃)'].iloc[-1]-file['周温差(℃)'].iloc[-2]:+.2f} °C", 
                 border=True)
        
        # 最低温度指标
        f.metric("本周最低温", 
                 f"{file['周最低温(℃)'].iloc[-1]:.2f} °C", 
                 f"{file['周最低温(℃)'].iloc[-1]-file['周最低温(℃)'].iloc[-2]:+.2f} °C", 
                 border=True)
    
    return