import pandas as pd
import numpy as np
import os
from datetime import date

os.chdir('C:/Users/Ynche/Downloads/DBuster2/Agglomerated')
weather_report = pd.read_csv('15614099999 hourly.csv',sep=',',usecols=['DATE', 'REPORT_TYPE','WND','TMP', 'SLP', 'AA1','AJ1'])

print('Shape of raw dataset {}'.format(weather_report.shape))
print('Types of raw dataset:\n{}'.format(weather_report.dtypes))
print('Description of raw dataset:\n{}'.format(weather_report.describe()))

weather_report = weather_report.rename(columns={'DATE': 'DATETIME'})
weather_report[['DATE','TIME']] = weather_report.DATETIME.str.split("T",expand=True)
weather_report.DATETIME = pd.to_datetime(weather_report.DATETIME, format='%Y-%m-%dT%H:%M:%S')
weather_report['WIND'] = weather_report.apply(lambda row: np.nan if int(row.WND[8:12])==9999 or not row.WND[8:12].isdigit() else int(row.WND[8:12]), axis=1)
weather_report['TEMP'] = weather_report.apply(lambda row: np.nan if int(row.TMP[0:5])== 9999 else int(row.TMP[0:5])/10, axis=1)
weather_report['PRESSURE'] = weather_report.apply(lambda row: np.nan if int(row.SLP[0:5])==99999 else int(row.SLP[0:5]), axis=1)
weather_report['AA1'] = weather_report.apply(lambda row: np.nan if row.AA1==np.nan else str(row.AA1), axis=1)
weather_report['AJ1'] = weather_report.apply(lambda row: np.nan if row.AJ1==np.nan else str(row.AJ1) , axis=1)
weather_report['SNOW'] = weather_report.apply(lambda row: 0 if row.AJ1==np.nan or not row.AJ1[9:15].isdigit() or row.AJ1[9:15]=='999999'  else int(row.AJ1[9:15]), axis=1)
weather_report['RAIN'] = weather_report.apply(lambda row: np.nan if row.AA1==np.nan or not row.AA1[0:2]=='12' or not row.AA1[3:7].isdigit() or row.AA1[3:7] == '9999' else int(row.AA1[3:7]), axis=1)
# weather_report.PRESSURE = weather_report.PRESSURE.fillna(method='ffill')
fm12 = weather_report[['DATETIME', 'REPORT_TYPE', 'PRESSURE','SNOW', 'RAIN']].copy()
fm12.drop(fm12[fm12.REPORT_TYPE == 'FM-15'].index, inplace=True)
fm12.drop(fm12[fm12.REPORT_TYPE == 'FM-16'].index, inplace=True)
fm12.to_csv('fm12.csv')
weather_report.drop(weather_report[weather_report.REPORT_TYPE == 'FM-12'].index, inplace=True)
weather_report.drop(weather_report[weather_report.REPORT_TYPE == 'FM-16'].index, inplace=True)

days = pd.date_range(date(2017,1,1), date(2019,12,31),freq = 'H')

climate = pd.DataFrame({'DATETIME': days})
climate = climate.set_index('DATETIME')
climate["WIND"] = weather_report.set_index('DATETIME').resample('H')['WIND'].mean().round(2)
climate["TEMP"] = weather_report.set_index('DATETIME').resample('H')['TEMP'].mean().round(2)
climate["PRESSURE"] = fm12.set_index('DATETIME')['PRESSURE']
climate["SNOW"] =fm12.set_index('DATETIME')['SNOW']
climate["RAIN"] = fm12.set_index('DATETIME')['RAIN']
climate["RAIN"].bfill(limit=11,inplace = True)
climate["SNOW"].bfill(limit=2,inplace = True)
climate["PRESSURE"].bfill(limit=2,inplace = True)
climate.RAIN = round(climate.RAIN/12,2)
climate.SNOW = round(climate.SNOW/3,2)
climate.SNOW.fillna(value=0,inplace = True)
climate.RAIN.fillna(value=0,inplace = True)


climate.to_csv('climate.csv')

print('Shape of final dataset {}'.format(climate.shape))
print('Types of final dataset:\n{}'.format(climate.dtypes))
print('Description final dataset:\n{}'.format(climate.describe()))
