# -*- coding: utf-8 -*-
"""
文件上传模块
功能：提供站点数据文件上传功能
Created on Wed Aug 13 13:30:16 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import streamlit as st
import os
from utils.load_station_data import load_station_data

def save_uploaded_file(uploaded_file, filename, directory="./station/"):
    """
    保存上传的文件到指定目录
    参数:
        uploaded_file: 上传的文件对象
        filename (str): 保存的文件名
        directory (str): 保存目录
    返回:
        str: 文件保存路径（成功）或 None（失败）
    """
    try:
        # 保存文件
        file_path = os.path.join(directory, filename)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        st.error(f"文件保存失败: {e}")
        return None

@st.dialog("upload files")  # Streamlit对话框装饰器
def upload_files():
    """文件上传对话框"""
    st.write("请选择要上传的文件")
    
    # 选择地图区域
    projection_option = st.selectbox("请选择地图区域", ("南极", "北极"), key='dialog1')
    df = load_station_data(projection_option)
    
    # 选择国家
    countries = df['Party'].unique().tolist()
    selected_country = st.selectbox("请选择一个国家", countries, index=None, key='dialog2')
    
    # 选择站点
    if selected_country:
        filtered_df = df[df['Party'] == selected_country]
        station_names = filtered_df['Name'].tolist()
        selected_station = st.selectbox("请选择一个站点", station_names, index=None, key='dialog3')
    else:
        selected_station = None
    
    # 文件上传组件
    uploaded_file = st.file_uploader(
        "选择文件", 
        type=["xlsx"],  # 限制文件类型
        label_visibility="collapsed"
    )
    
    # 处理文件上传
    if uploaded_file is not None:
        if selected_station is None:
            file_name = uploaded_file.name
            st.warning('请确保文件名和站点名一致')
        else:
            file_name = selected_station + '.xlsx'
        
        # 保存文件
        if st.button('上传'):
            file_path = save_uploaded_file(uploaded_file, file_name)
            if file_path:
                # 保存上传状态到会话状态
                st.session_state.last_upload = {
                    "filename": uploaded_file.name,
                    "path": file_path,
                    "size": uploaded_file.size
                }
                st.success(f"文件已成功保存至: {file_path}")
    else:
        st.warning("请先选择文件")