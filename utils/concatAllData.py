import os
import glob
import pandas as pd
import numpy as np


path = "/home/tbh/Documents/windPrediction/Data"                                               
allFiles = glob.glob(os.path.join(path,"*.csv"))
cities = ['AMASYA','KIRLARELI','TEKIRDAG','EDIRNE','BURSA','SIVAS','BILECIK','AYDIN','HATAY','TOKAT','KONYA','GAZIANTEP','OSMANIYE','ISTANBUL','CNK','MUGLA','YALOVA','ADIYAMAN','KOC','KAYSERI','ISPARTA','USAK','MERSIN','IZMIR','MANISA','AFYON']

i = 0
for city in allFiles:

    globals()[l[i]] = pd.read_csv(city,usecols = ['Tarih','Saat','Toplam (MWh)'])
    globals()[l[i]]=globals()[l[i]].stack().str.replace(',','.').unstack()
    globals()[l[i]]['Toplam (MWh)'] = globals()[l[i]]['Toplam (MWh)'].astype('float64')
    i+=1

#SWEPT,NUMBER_OF_TURBINE
AMASYA_ = [12469 , 14]
ADIYAMAN_ = [7823,11]
AFYON_ = [9161,81]
AYDIN_ = [9852,15]
BILECIK_ = [7823,16]
BURSA_ = [9852,17]
CNK_ = [8332,19]
EDIRNE_ = [10000,16]
GAZIANTEP_ = [12469,19]
HATAY_ = [12305,19]
ISPARTA_ = [8332,36]
ISTANBUL_ = [5281,12]
IZMIR_ = [8332,21]
KAYSERI_ = [10715,19]
KIRLARELI_ = [10000,19]
KOC_ = [8332,6]
KONYA_ = [13685,24]
MANISA_ = [8332,16]
MERSIN_ = [8000,13]
MUGLA_ = [10000,25]
OSMANIYE_ = [7854,54]
SIVAS_ = [10207,6]
TEKIRDAG_ = [10715,15]
TOKAT_ = [10000,10]
USAK_ = [6421,36]
YALOVA_ = [6421,36]

def windVelocity(p , numberOfTurbines,cp,rho,swept):
    den = cp*rho*swept
    num = 2*(p / numberOfTurbines)*10**6
    v = num/den
    v = v**(1./3)
    v = v
    return v

cp = 0.4
rho = 1.24
for i in l:
    globals()[i+'Results'] = []

for i in l:
    globals()[i+'Results'] = np.array(globals()[i+'Results'])
for city in l:
    globals()[city][city + ' WindSpeed(m/s)'] = globals()[city+'Results']
for i in l:
    cityName = i 
    globals()[i].to_csv("/home/tbh/Documents/windPrediction/Data/{}.csv".format(i+'WindspeedData'))


