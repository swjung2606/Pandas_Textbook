# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 22:36:42 2022

@author: swjun
"""

import pandas as pd
from IPython.display import Image


# 철도 sheet 의 데이터를 가져온다.
excel = pd.read_excel('seoul_transportation.xlsx', sheet_name='철도', engine='openpyxl')
# 버스 sheet 의 데이터를 가져온다.
excel1 = pd.read_excel('seoul_transportation.xlsx', sheet_name='버스')
# 파일 안에 있는 모든 sheet 의 데이터를 가져온다.
excel2 = pd.read_excel('seoul_transportation.xlsx', sheet_name=None)


# 철도 데이터의 첫 번째 value 의 승차총승객수 + 버스 데이터의 네 번째 value 의 승차총승객수
print(excel2['철도'].iloc[0].승차총승객수 + excel2['버스'].iloc[3].승차총승객수)

# sample1 이라는 파일명으로 엑셀로 저장. 이때 index=False 는 인덱스가 별도의 열로 들어가는 것을 막는 기능.
excel.to_excel('sample1.xlsx', index=False, sheet_name='샘플')

# 여러 개의 시트에 저장하기 위해서 ExcelWriter 를 이용.
writer = pd.ExcelWriter('sample2.xlsx')
excel.to_excel(writer, index=False, sheet_name='샘플1')
excel.to_excel(writer, index=False, sheet_name='샘플2')
excel.to_excel(writer, index=False, sheet_name='샘플3')
writer.close()



############### CSV File ##############

df = pd.read_csv('seoul_population.csv')

# 데이터의 크기가 큰 경우 chucksize 를 이용하여 데이터를 분리해서 load 가능

df = pd.read_csv('seoul_population.csv', chunksize=10)
for d in df:
    display(d)



