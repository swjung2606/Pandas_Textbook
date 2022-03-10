# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 11:00:54 2022

@author: swjun
"""

from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')


# Switch data value by using apply

# First, define a definition
def transform_who(x):
    if x == 'man':
        return 'M'
    elif x== 'woman':
        return 'F'
    else:
        return 'Child'

# It changes 'man', 'woman', 'child' to 'M', 'F', 'Child' respectively.
df['who'].apply(transform_who)



# We can also compute numerical data.
def Fare_Age_Ratio(x):
    return x['fare'] / x['age']

df.apply(Fare_Age_Ratio, axis=1)


# We can also use lambda function
# It changes 0 and 1 to 'dead' and 'alived' respectively.
df['survived'].apply(lambda x: 'alived' if x==1 else 'dead')



# We can see the statistical values based on group by using groupby
df.groupby('sex').mean()
df.groupby('survived').mean()
df.groupby(['embark_town','sex']).mean()

# It shows 'survived' column only.
df.groupby(['embark_town','sex'])['survived'].mean()
df.groupby(['sex','pclass'])[['survived','age']].mean()
df.groupby(['sex','pclass'])[['survived','age']].agg(['mean','median','std'])




####### pivot_table part #######
# It is intuitive! So I prefer this!


df.pivot_table(index='who' , values='survived') # values are showing mean values.
df.pivot_table(columns='who' , values='survived')

df.pivot_table(index=['who','pclass'] , values='survived')
df.pivot_table(columns=['who','pclass'] , values='survived')

df.pivot_table(index=['who','pclass'] , values=['survived','age'])
df.pivot_table(columns=['who','pclass'] , values=['survived','age'])

df.pivot_table(index='who' , columns='pclass' , values='survived')
df.pivot_table(index='who' , columns='pclass' , values='fare' , aggfunc=['mean','std'])















