# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 23:27:12 2022

@author: swjun
"""

import pandas as pd
from IPython.display import Image
import numpy as np
import seaborn as sns


df = sns.load_dataset("titanic")

# It shows the columns information
df.info()

# It shows numerical type column's statistical information
df.describe()

# It shows 'object' data type column's information
df.describe(include='object')

# It shows the detail information of the column 'embarked'
df['embarked'].value_counts()

# It shows all data with numpy array form
df.values

# It changes the type of data of 'pclass' from int64 to int32
df['pclass'].astype('int32')

# It can sort the data by 'age'
df.sort_values(by='age')
df.sort_values(by='pclass', ascending=False) # Reverse order
df.sort_values(by=['age','pclass']) # Sorting by age and pclass
df.sort_values(by=['age','pclass'], ascending=[True,False])




################# condition filtering #################

# Indexing part
df.loc[5]
df.loc[5,'class'] # just showing class column value
df.loc[1:3, ['age','class','fare']] # showing values from 1 to 3 with the three column values

# Slicing part
df.loc[1:5, 'fare':'class']  # Choose from 'fare' to 'class' columns of index 1 to 5. 


# Condition filtering
df[df['who']=='man'] # showing who = man data only

# Multi conditions
condition1 = df['fare'] > 30      # first condition
condition2 = df['who'] == 'woman' # second condition
condition3 = df['pclass'] == 1    # third condition

df.loc[condition1 & condition2 & condition3]   # showing values that satisfy those conditions.
df.loc[condition1 & condition2 | condition3]   # condition1 and condition2 or condition3


# Among values that satisfy condition1 and condition2, showing this based on fare ascending order.
df.loc[condition1 & condition2].sort_values(by='fare', ascending=False)



cond1 = df['age'] >= 20
cond2 = df['age'] < 40
cond3 = df['pclass'] == 1
cond4 = df['pclass'] == 2

# Data conditions -> cond1 ~ cond4 , showing four columns ['survived','pclass','age','fare'] only
       # Condition part                      # Wanted columns list
df.loc[ (cond1 & cond2) & (cond3 | cond4) , ['survived','pclass','age','fare'] ]
 
# where command

# if the value of fare is less than 20, it would be replaced with 0 value.
df['fare'].where(df['fare']>20 , 0)

# Add one more columns named 'survival'
df['survival'] = 'None'
# if the value of 'survived' column is equal to 1, 'survival' column value would be replaced with 'survived!
df['survival'] = df['survival'].where(df['survived']==0, 'survived!')


