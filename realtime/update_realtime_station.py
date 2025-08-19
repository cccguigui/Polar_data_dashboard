# -*- coding: utf-8 -*-
"""
实时气象站数据更新模块
功能：爬取最新周报数据并更新本地存储
Created on Thu Aug 14 09:19:59 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import streamlit as st  # 用于构建Web应用
import pandas as pd  # 数据处理库
from datetime import timedelta  # 时间计算
import re  # 正则表达式库
from realtime.find_weekly_reports import find_weekly_reports  # 本地模块
from realtime.extract_weather_data import extract_weather_data  # 本地模块

@st.dialog("更新周数据")
def update_realtime_station():
    """更新实时气象站数据的对话框函数"""
    with st.container(height=300):
        with st.status("爬取数据中...", expanded=True) as status:
            # 第一步：获取所有周报链接
            st.write("开始扫描周报链接...")
            weekly_reports = find_weekly_reports()
            st.write(f"\n共找到 {len(weekly_reports)} 个周报")
            
            # 第二步：提取每个周报的气象数据
            st.write("\n开始提取气象数据...")
            all_data = []  # 存储所有站点数据
            
            for title, url in weekly_reports:
                st.write(f"处理周报: {title}")
                weather_data = extract_weather_data(url)  # 提取气象数据文本
                
                # 使用正则表达式提取各站点数据
                station_pattern = r'【(.*?)】([^【]+)'
                stations = re.findall(station_pattern, weather_data)
                
                # 解析每个站点的详细数据
                for station_name, station_data in stations:
                    # 提取基本信息
                    time_match = re.search(r'更新时间:(\d{4}-\d{2}-\d{2} \d{2}:\d{2})', station_data)
                    temp_match = re.search(r'温度([-\d.]+)\(℃\)', station_data)
                    humidity_match = re.search(r'湿度([-\d.]+)\(%\)', station_data)
                    pressure_match = re.search(r'气压([-\d.]+)\(mb\)', station_data)
                    wind_dir_match = re.search(r'风向([^,]+),', station_data)
                    wind_speed_match = re.search(r'风速([-\d.]+)\(m/s\)', station_data)
                    
                    # 提取周统计信息
                    temp_diff_match = re.search(r'温差([-\d.]+)℃', station_data)
                    min_temp_match = re.search(r'最低([-\d.]+)℃', station_data)
                    
                    # 添加到数据列表
                    all_data.append({
                        "站点名称": station_name,
                        "更新周数": title[7:-1],  # 提取周数信息
                        "更新时间": time_match.group(1) if time_match else None,
                        "温度(℃)": float(temp_match.group(1)) if temp_match else None,
                        "湿度(%)": float(humidity_match.group(1)) if humidity_match else None,
                        "气压(mb)": float(pressure_match.group(1)) if pressure_match else None,
                        "风向": wind_dir_match.group(1) if wind_dir_match else None,
                        "风速(m/s)": float(wind_speed_match.group(1)) if wind_speed_match else None,
                        "周温差(℃)": float(temp_diff_match.group(1)) if temp_diff_match else None,
                        "周最低温(℃)": float(min_temp_match.group(1)) if min_temp_match else None,
                        "周报URL": url,
                    })
            
            # 创建DataFrame
            df = pd.DataFrame(all_data)
            # 将更新时间列转换为datetime格式
            df['更新时间'] = pd.to_datetime(df['更新时间'])
            # 计算起始时间（更新时间减去7天）
            df['起始时间'] = (df['更新时间'] - timedelta(days=7)).dt.date
            df['结束时间'] = (df['更新时间'] - timedelta(days=1)).dt.date
            
            # 调整列顺序
            move_cols = df.pop('起始时间')
            df.insert(3, '起始时间', move_cols)
            move_cols = df.pop('结束时间')
            df.insert(4, '结束时间', move_cols)
            
            # 保存为CSV文件
            status.update(label='保存数据到"./station/极地周气象数据/极地气象数据.csv"...', expanded=True)
            csv_filename = "./station/极地周气象数据/极地气象数据.csv"
            df.to_csv(csv_filename, index=False, encoding='utf_8_sig')
            st.write(f"\n数据已保存到 {csv_filename}")
            
            # 保存为Excel文件（按站点分Sheet）
            status.update(label='保存数据到"./station/极地周气象数据/极地气象数据.xlsx"...', expanded=True)
            excel_filename = "./station/极地周气象数据/极地气象数据.xlsx"
            with pd.ExcelWriter(excel_filename) as writer:
                # 获取所有站点名称
                unique_stations = df['站点名称'].unique()
                
                for station in unique_stations:
                    # 过滤当前站点的数据
                    station_df = df[df['站点名称'] == station]
                    
                    # 按更新时间排序
                    station_df = station_df.sort_values(by='更新时间')
                    
                    # 将当前站点数据写入单独Sheet
                    sheet_name = station[:31]  # Excel表名限制31字符
                    station_df.to_excel(writer, sheet_name=sheet_name, index=False)
                    st.write(f"  已保存 {station} 站点数据到 Sheet: {sheet_name}")
            
            st.write(f"数据已保存到 {excel_filename}")
            status.update(label="更新完成!", state="complete", expanded=False)