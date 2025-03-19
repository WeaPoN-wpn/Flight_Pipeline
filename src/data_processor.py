import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def clean_data(df):
    df = df.copy()
    # 处理目标列缺失值（用均值填充）
    if 'ArrDelayMinutes' in df.columns:
        df['ArrDelayMinutes'] = df['ArrDelayMinutes'].fillna(df['ArrDelayMinutes'].mean())
    # 填充 DepDelay 均值
    if 'DepDelay' in df.columns:
        df['DepDelay'] = df['DepDelay'].fillna(df['DepDelay'].mean())
    # 填充 TaxiOut 缺失为0（滑行时间）
    if 'TaxiOut' in df.columns:
        df['TaxiOut'] = df['TaxiOut'].fillna(0)
    # 其他简单缺失处理
    df.ffill(inplace=True)
    return df

def feature_engineering(df):
    df = df.copy()
    
    # 时间特征提取
    if 'CRSDepTime' in df.columns:
        df['CRSDepHour'] = (df['CRSDepTime'] // 100).astype(int)
    if 'CRSArrTime' in df.columns:
        df['CRSArrHour'] = (df['CRSArrTime'] // 100).astype(int)

    # 类别特征编码（严格对齐你的建模代码）
    for col in ['Airline', 'Origin', 'Dest']:
        if col in df.columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
    
    return df