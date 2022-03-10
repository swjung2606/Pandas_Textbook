# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:10:45 2022

@author: swjun
"""
from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns


df = sns.load_dataset('titanic')

# copy the DataFrame
df_copy = df.copy()

# modify the data
df_copy.loc[0,'age'] = 999

# it shows all NaN values in each column
df.isnull().sum()

# it shows all values that have NaN value with 'age' column.
df.loc[df['age'].isnull()]


'''
# fill all NaN data of age with 30
nan_list = df.loc[df['age'].isnull()]['age'].index # index of values who have NaN with 'age'

for i in nan_list:
    df.loc[i , 'age'] = 30
'''


'''
# fillna() can fill all NaN values for a certain column
df['age'] = df['age'].fillna(700)
'''

'''
# fill all NaN values of 'age' column with mean of non-NaN ages
df['age'] = df['age'].fillna( df['age'].mean() )
'''

df1 = df.copy()

# it deletes the values(rows) that are including NaN value for any columns.
df1.dropna()

# it deletes all columns that are including NaN values.
df1.dropna(axis=1)

# it deletes the values(rows) that include NaN value on their 'age' columns
df1.dropna(subset=['age'])

# it deletes the values(rows) that include NaN value on either 'age' or 'deck'
df1.dropna(subset=['age','deck'])

# it deletes the values(rows) that include NaN values on both 'age' and 'deck'
df1.dropna(subset=['age','deck'], how='all')



