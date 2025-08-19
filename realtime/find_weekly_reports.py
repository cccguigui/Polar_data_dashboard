# -*- coding: utf-8 -*-
"""
周报链接查找模块
功能：爬取极地研究中心网站获取周报链接
Created on Thu Aug 14 09:51:58 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import requests  # HTTP请求库
from bs4 import BeautifulSoup  # HTML解析库
import re  # 正则表达式库
from urllib.parse import urljoin  # URL处理工具
import streamlit as st  # 用于构建Web应用

def find_weekly_reports():
    """
    查找所有两极环境周报链接
    返回:
        list: 包含(标题, URL)的元组列表
    """
    base_url = "https://pole.whu.edu.cn/cn/gb_news.php?modid=02001&pageid={}"
    reports = []  # 存储找到的周报
    
    # 遍历可能的页面ID范围
    for page_id in range(1, 1000):
        url = base_url.format(page_id)
        try:
            # 发送HTTP请求
            response = requests.get(url, timeout=10)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 查找所有class="hover-blue"的链接
            links = soup.select('a.hover-blue')
            for link in links:
                title = link.get_text().strip()
                # 匹配标题格式：两极环境周报（XXXX年第XX周）
                if re.match(r'两极环境周报\(\d{4}年第\d{1,2}周\)', title):
                    href = link.get('href')
                    # 处理相对路径为完整URL
                    full_url = urljoin(url, href)
                    reports.append((title, full_url))
                    
            # 显示扫描进度
            st.write(f"已扫描 pageid={page_id}, 找到{len(reports)}个周报")
            
            # 如果没有找到链接则停止扫描
            if not links:
                break
                
        except Exception as e:
            st.write(f"处理pageid={page_id}时出错: {str(e)}")
            break
    
    return reports