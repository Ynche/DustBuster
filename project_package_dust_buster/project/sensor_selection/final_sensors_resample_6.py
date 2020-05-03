import pandas as pd
import os

os.chdir('C:/Users/Ynche/Downloads/DBuster2/Agglomerated')
sensors_df = pd.read_csv("sensors_df.csv")

sensors_df.dtime = pd.to_datetime(sensors_df.dtime)
sensors_df['date'] = pd.to_datetime(sensors_df.dtime.dt.date)
sensors_df['hour'] = sensors_df.dtime.dt.hour
sensors_df['weekday'] = sensors_df.dtime.dt.weekday
sensors_df['weekdayname'] = sensors_df.dtime.dt.weekday_name
sensors_df['month'] = sensors_df.dtime.dt.month
# sensors_df['date'] = pd.to_datetime(sensors_df.date)
sensors_final_dataset=sensors_df[~sensors_df.date.isin(pd.date_range(start='20150101', end='20170930'))]

sensors_final_dataset.to_csv('sensors_final_dataset.csv')

print('Shape of final dataset {}'.format(sensors_final_dataset.shape))
print('Types of final dataset:\n{}'.format(sensors_final_dataset.dtypes))
print('Description final dataset:\n{}'.format(sensors_final_dataset.describe()))