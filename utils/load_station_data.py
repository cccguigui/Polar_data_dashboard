# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 13:51:46 2025

@author: Chu Jiawen
@email：cjw0206@foxmail.com
"""

import pandas as pd

def load_station_data():
    url = "./station/PermanentStations.csv"
    df = pd.read_csv(url)
    df = df[['Name', 'Latitude', 'Longitude', 'Party']].dropna()
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)
    return df