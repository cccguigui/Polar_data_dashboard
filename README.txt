# 极地气象数据监控系统

## 项目概述
本系统是一个集数据采集、处理和可视化于一体的极地气象数据监控平台，主要功能包括：
- 实时爬取并解析极地研究中心发布的周报数据
- 多站点气象数据展示与对比分析
- 极地区域气象要素空间分布可视化
- 公司站点数据管理与分析
- 历史数据趋势分析

## 环境配置
1. **Python版本**: 3.9+
2. **安装依赖**:
   ```bash
   pip install -r requirements.txt
3. **数据准备**:
创建必要的目录结构：
   ```bash
mkdir -p station/极地周气象数据
mkdir -p station/公司站点数据
## 项目结构
polar-weather/
├── realtime/                  # 实时数据模块
│   ├── display_data_table.py  # 数据展示
│   ├── extract_weather_data.py# 数据提取
│   ├── find_weekly_reports.py # 周报采集
│   ├── update_realtime_station.py # 数据更新
│   ├── update_time.py         # 时间记录
│   └── update_time.txt        # 更新时间记录
├── utils/                     # 工具模块
│   ├── create_dual_axis_plot.py # 双轴图表
│   ├── create_single_line_plot.py # 单线图表
│   ├── display_data_table.py  # 数据表格展示
│   ├── draw_countorf.py       # 等值线图绘制
│   ├── draw_map_base.py       # 基础地图
│   ├── feature_plots.py       # 特征指标展示
│   ├── is_in_dir.py           # 目录检查
│   ├── load_station_data.py   # 站点数据加载
│   ├── process_company_data.py # 公司数据处理
│   ├── process_data.py        # 数据处理
│   ├── render_data.py         # 数据渲染
│   ├── render_plots.py        # 图表渲染
│   ├── update_station_points.py # 站点标记
│   ├── update_variable_field.py # 变量场更新
│   └── upload_files.py        # 文件上传
├── station/                   # 数据存储
│   ├── 极地周气象数据/          # 气象数据集
│   ├── 公司站点数据/            # 公司提供数据
│   ├── Antarctic.csv          # 南极站点数据
│   ├── Arctic.csv             # 北极站点数据
│   └── wind_temperature.csv   # 风温数据
├── main.py                    # 主程序入口
├── polar_station_tab.py       # 极地站点标签页
├── company_station_tab.py     # 公司站点标签页
├── real_time_tab.py           # 实时数据标签页
├── requirements.txt           # 依赖清单
└── README.md                  # 项目文档

## 使用说明
1. **启动应用**: `streamlit run main.py`
2. **数据更新**:
   - 在"实时数据"标签页点击"更新周数据"按钮
   - 手动上传站点数据到`./station/`目录
3. **数据查看**:
   - 极地站点数据: 选择区域、国家、站点查看数据
   - 公司站点数据: 选择数据类型和时间范围
   - 实时数据: 查看最新气象数据和网站嵌入

## 注意事项
1. GitHub不支持空文件夹，请确保所有目录包含至少一个文件
2. 首次运行前需安装所有依赖
3. 数据更新需要网络连接访问外部数据源