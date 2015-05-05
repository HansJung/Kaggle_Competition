# -*- coding: utf-8 -*-
'''
Goal : To study how to use XGBoost
Author : Yonghan Jung, IE, KAIST 
Date : 150502
Comment 
- 
'''

''' Library '''
import math
import csv
import numpy as np

''' Function or Class '''
def Sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

# build weather dic
Ntrain = 10506
Ntest = 116293
Nfea = 13
MISSING = 999.0
# Feature: Month, Week, Latitude, Longitude, NumMosq in Nearest Area, Near Dis, TMax, Tmin, Tavg, WaterBub, Dry, StnPressure

Xtrain = np.zeros((Ntrain, Nfea), dtype=np.float32)
Ytrain = []
Xtest = np.zeros((Ntest, Nfea), dtype=np.float32)

train_head = ""
spray_head = ""
weather_head = ""
weather_dic = {}
train_dic = {}

fi = csv.reader(open("../input/weather.csv"))
weather_head = fi.__next__()
for line in fi:
    # simply discard station 1
    if line[0] == '1':
        continue
    weather_dic[line[1]] = line

if __name__ == "__main__":
    print None
