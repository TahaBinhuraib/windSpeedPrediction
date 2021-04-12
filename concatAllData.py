import os
import glob
import pandas as pd
import numpy as np

path = "/home/tbh/Documents/windPrediction/Data"

all_files = glob.glob(os.path.join(path, "*.csv"))     
df_from_each_file = (pd.read_csv(f) for f in all_files)
df = pd.merge(df_from_each_file , how = "left",on=["Tarih","Saat"])








print(df.head())



