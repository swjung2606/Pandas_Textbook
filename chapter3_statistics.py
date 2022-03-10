# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 14:05:24 2022

@author: swjun
"""

from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

# it shows statistical information for numerical data
df.describe()

# it shows statistical information for object data
df.describe(include='object')

# it shows the number of data for a certain column.
df.count()
df['age'].count()

# it shows the mean of a certain column
df.mean()
df['age'].mean()
df.loc[df['pclass']==1, 'age'].mean()

# it shows the median of a certain column
df['age'].median()

# it shows the sum of a certain column
df['pclass'].sum()

# it shows the cumulative value of a certain column
df['pclass'].cumsum()

# it shows the variance of a certain column
df['pclass'].var()

# it shows the standard deviation of a certain column
df['fare'].std()

# it shows the min & max value of a certain column
df['fare'].min()
df['fare'].max()

# it shows the kurtosis level of data of a certain column
df.kurtosis()

# it shows the skew level of data of a ceratin column. We can visualize this by using histplot.
df['age'].skew()
sns.histplot(df['age'])

# We can see any kind of statistical data by using agg()
df['age'].agg(['min','max','mean','std','median'])
df[['age','fare']].agg(['mean','std','median','kurtosis','skew'])

# it shows upper x percent value of a certain column.
df['fare'].quantile(0.2)
df['fare'].quantile(0.9)

# it shows the number of components of a certain column
df['embarked'].unique()
df['embarked'].nunique()

# Correlation code examples
df['age'].corr(df['fare'])  # correlation value between 'age' and 'fare' data



