# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 11:06:02 2022

@author: swjun
"""

from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

# Add 'VIP' column to df
df['VIP'] = True
df.insert(0,'Test',True) # add 'Test' column to 0th column with having value True

# Delete row. It deletes the value(row) of index 1
df.drop(1)
df.drop(np.arange(10)) # delete the rows from 0 to 9
df.drop([1,3,5,7,9]) # delete the rows 1,3,5,7,9

# Delete column.
df.drop('embarked', axis=1)  # delete 'embarked' column
df.drop(['who','deck','alive'], axis=1) # delete 'who', 'deck', 'alive' columns

# Add two columns to generate new column named 'family'
df['family'] = df['sibsp'] + df['parch']

# We can also add two strings columns.
df['gender'] = df['who'] + '-' + df['sex']

# Define 소수점자리 by round
df['round'] = round(df['fare'] / df['age'] , 2)

# Change the data type to 'int32'
df['pclass'].astype('int32')


# Date
# https://wikidocs.net/136681
date = pd.date_range('20220101', periods = df.shape[0] , freq='15H')
df['date'] = date


# Assign the level of numerical data based on bins we set.
bins = [0,30,60,90] # 0~30 / 30~60 / 60~90
labels = ['Young', 'Middle', 'Old']
pd.cut(df['age'], bins, labels=labels, right=False)
