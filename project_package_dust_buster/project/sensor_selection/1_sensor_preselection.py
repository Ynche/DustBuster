import pandas as pd
from project.function_modules.functions_general import apply_location_criteria
import numpy as np


# Remark: the '2019-12_sds011' csv file is not included in the package (size 9.94 GB).It can be downloaded from https://archive.luftdaten.info/csv_per_month/2019-07/
latitude:str = 'lat'
longitude:str = 'lon'
MAX_LAT = 42.75
MIN_LAT = 42.64
MAX_LON = 23.42
MIN_LON = 23.23


chunk_list = pd.DataFrame(columns=['sensor_id','lat','lon'])
for chunk in pd.read_csv("2019-12_sds011.csv",chunksize=100000,sep=";",usecols = ['sensor_id','lat','lon'],dtype={'sensor_id': np.object_, 'lat': np.float64, 'lon': np.float64}):
    chunk_filtered = apply_location_criteria(chunk,MAX_LAT,MIN_LAT,MAX_LON,MIN_LON) # we apply the location criteria to filter only sensors in Sofia
    chunk_list= pd.concat([chunk_list,chunk_filtered],axis=0, join='outer', ignore_index=False)
chunk_list = chunk_list.drop_duplicates(subset='sensor_id', keep="first")
chunk_list.to_csv('chunk_list.csv')
df = pd.read_csv('chunk_list.csv', sep=",")
df = df.drop_duplicates(subset='sensor_id', keep="first")
df.to_csv('df_concat.csv')
print(df.shape) #(352, 3) A dataframe with unique sensors in Sofia city
