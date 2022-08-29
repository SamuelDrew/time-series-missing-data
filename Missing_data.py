#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
import numpy as np
import re
from datetime import datetime
def calcMissing(readings):
 data = []
 missing = []
 predictions  = []
 
 #process data
 for i in range(readings_count):
    x = readings[i].strip().split('\t')
    x = list(filter(None, x))    
    data.append([pd.to_datetime(x[j]) if j == 0 else x[j] for j in range(len(x))])
 #construct dataframe   
 data = pd.DataFrame(data, columns = ['Date/Time', 'MercLvl'])
 missingData = data[data['MercLvl'].str.contains('Missing')]
 data = pd.merge(data,missingData,indicator = True, how = 'outer').query('_merge == "left_only"').drop('_merge', axis = 1)
 data = data.reset_index(drop = True)
 mRows = missingData.loc[:, missingData.columns!='MercLvl']
 t = data
 test = mRows
 #construct & fit prediction model
 gbr = GradientBoostingRegressor(n_estimators = 100, learning_rate = 0.5, max_depth = 2)
 gbr.fit(t.loc[:,t.columns!= 'MercLvl'], t.loc[:,'MercLvl'])
 #predict
 for i,j in enumerate(gbr.predict(test)):
    predictions.append((test.index[i],round(j,1)))
 for k in range(len(predictions)):
    print(predictions[k][1])
