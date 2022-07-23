# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:23:09 2022

@author: Sungwoo Jung
"""

import numpy as np
import pandas as pd
import seaborn as sns



########## Useful command in Python ##########

# Load Titanic Data
ti = sns.load_dataset('titanic')


### 1. Fill NA of 'age' column by 'sex'
ti.loc[ti['sex']=='male', 'age'] = ti.loc[ti['sex']=='male', 'age'].fillna(ti.loc[ti['sex']=='male', 'age'].mean())
ti.loc[ti['sex']=='female', 'age'] = ti.loc[ti['sex']=='female', 'age'].fillna(ti.loc[ti['sex']=='female', 'age'].mean())


### 2. Remove all rows with value "no" in alive column
ti = ti.loc[ti['alive']=='yes']


### 3. Remove all rows that include NA in 'embark_town' column
ti = ti.dropna(subset=['embark_town'])


### 4. Get unique array for 'embark_town'
WaferId = np.unique(ti['embark_town'])


########## 5. Very Very Useful Expression!!! Define multiple variables in loop ##########

# It defines variables 
# Wafer_Cherbourg = ti.loc[ti['embark_town']=='Cherbourg' , 'age'].mean()
# Wafer_Queenstown = ti.loc[ti['embark_town']=='Queenstown' , 'age'].mean()
# Wafer_Southampton = ti.loc[ti['embark_town']=='Southampton' , 'age'].mean()

for i in WaferId:
    exec( f"Wafer_{i} = ti.loc[ti['embark_town']==i , 'age'].mean()" )


### 6. Application!

WaferStageId = np.unique(ti['sex'])
DataType = np.unique(ti['pclass'])


# It generates variables such as
# common_female_2_Queenstown = ti.loc[ti['pclass']== i, 'age'].median()
for h in WaferStageId:
    for i in DataType:
        for j in WaferId:
            exec( f"common_{h}_{i}_{j} = ti.loc[ti['pclass']== i , 'age'].median()" )
            

