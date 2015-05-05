# -*- coding: utf-8 -*-
'''
Goal : DataRead
Author : Yonghan Jung, ISyE, KAIST 
Date : 150505
Comment 
- 

'''

''' Library '''
import numpy as np
import pandas as pd
from collections import Counter
''' Function or Class '''


class DataReader:
    def __init__(self):
        pass
    def TrainDataRead(self):
        DataRead = pd.read_csv('train.csv')[["Date","Address","Species","Block","Street","Trap","AddressNumberAndStreet","Latitude","Longitude","AddressAccuracy","NumMosquitos","WnvPresent"]]
        return DataRead

    def TestDataRead(self):
        DataRead = pd.read_csv('test.csv')[["Date","Address","Species","Block","Street","Trap","AddressNumberAndStreet","Latitude","Longitude","AddressAccuracy"]]
        return DataRead

    def SprayData(self):
        DataRead = pd.read_csv('spray.csv')[["Date","Latitude","Longitude"]]
        return DataRead

    def WeatherData(self):
        DataRead = pd.read_csv('weather.csv')[["Station","Date","Tmax","Tmin","Tavg","Depart","DewPoint","WetBulb","Heat","Cool","Sunrise","Sunset","CodeSum","Depth","Water1","SnowFall","PrecipTotal","StnPressure","SeaLevel","ResultSpeed","ResultDir","AvgSpeed"]]
        return DataRead

if __name__ == "__main__":
    Data = DataReader()
    TrainData = Data.TrainDataRead()
    SprayData = Data.SprayData()
    WeatherData = Data.WeatherData()

    TestData = Data.TestDataRead()
    WNVData = TrainData[(TrainData.WnvPresent == 1)]




