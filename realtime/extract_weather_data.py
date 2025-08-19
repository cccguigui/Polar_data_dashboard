# -*- coding: utf-8 -*-
"""
气象数据提取模块
功能：从极地周报网页中提取气象数据
Created on Thu Aug 14 09:51:58 2025
@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""
import requests  # HTTP请求库
from bs4 import BeautifulSoup  # HTML解析库

def extract_weather_data(report_url):
    """
    从周报URL提取气象数据
    参数:
        report_url (str): 周报网页URL
    返回:
        str: 提取的气象数据文本
    """
    try:
        # 发送HTTP请求获取网页内容
        response = requests.get(report_url, timeout=10)
        response.encoding = 'utf-8'  # 设置编码格式
        soup = BeautifulSoup(response.text, 'html.parser')  # 创建BeautifulSoup对象
        
        # 查找包含"最新极地气象"的<h2>标签
        target_header = None
        for h2 in soup.find_all('h2'):
            if '最新极地气象' in h2.get_text():
                target_header = h2
                break
                
        # 未找到目标标题时返回错误信息
        if not target_header:
            return "未找到最新极地气象板块"
            
        # 收集气象数据
        weather_data = []
        # 从目标标题开始向后查找兄弟元素
        next_elem = target_header.find_next()
        
        while next_elem:
            # 查找符合样式的<font>标签
            if next_elem.name == 'font' and 'font-size:12px' in next_elem.get('style', ''):
                text = next_elem.get_text(strip=True)  # 获取清理后的文本
                # 检查文本格式（以【开头，以℃结尾）
                if text.startswith('【') and text.endswith('℃'):
                    weather_data.append(text)
            
            # 遇到分隔线或新标题则停止收集
            elif next_elem.name in ['h2', 'h3', 'hr']:
                break
                
            next_elem = next_elem.find_next_sibling()  # 移动到下一个兄弟元素
        
        # 返回拼接后的气象数据
        return '\n'.join(weather_data)
    except Exception as e:
        return f"提取数据出错: {str(e)}"