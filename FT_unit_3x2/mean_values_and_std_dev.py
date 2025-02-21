# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:05:45 2023

@author: 13471
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 从 CSV 文件中读取数据
#df = pd.read_csv('G:/Air_Mod_Robot/03ACAI_AirModBot/02AirModBotData/023x2_2unit/03_24/Position_Data_3x2_24_error_1to10.csv')
df = pd.read_csv('G:/Air_Mod_Robot/03ACAI_AirModBot/05AirModBotData_FT/Position_Data_3x2_34_error_1to10_my.csv')



# 计算每一行的均值和标准偏差
mean_values = df.mean(axis=1)
std_dev = df.std(axis=1)

# 创建一个新的 DataFrame 来存储均值和误差棒
df_new = pd.DataFrame({
    'Mean Values': mean_values,
    'Error Bars': std_dev
})


# 将新的 DataFrame 保存到 CSV 文件
df_new.to_csv('C:/Users/13471/Desktop/mean_error_3x2_34_error.csv', index=False)
