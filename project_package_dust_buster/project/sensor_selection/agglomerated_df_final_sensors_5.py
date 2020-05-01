import pandas as pd
import os
# from project.sensor_selection.filter_sensors_summary_4 import final_sensor_list

os.chdir('C:/Users/Ynche/Downloads/DBuster2')
# print(final_sensor_list)
# sensors_df = pd.DataFrame()
# for file in os.listdir(os.getcwd()):
#     index = file.rfind('_')
#     if file.endswith('.csv') and int(file[index+1:-4]) in final_sensor_list:
#         df = pd.read_csv(file, sep=";")
#         df['dtime'] = pd.to_datetime(df.timestamp)
#         new_df = pd.DataFrame()
#         new_df["P1"] = df.set_index('dtime').resample('H')['P1'].mean().round(2)
#         new_df["P2"] = df.set_index('dtime').resample('H')['P2'].mean().round(2)
#         new_df["sensor_id"] = df.sensor_id[0]
#         new_df["sensor_type"] = df.sensor_type[0]
#         new_df["location"] = df.location[0]
#         new_df["lat"] = df.lat[0]
#         new_df["lon"] = df.lon[0]
#         sensors_df = pd.concat([sensors_df,new_df])
# sensors_df.to_csv('Agglomerated/sensors_df.csv')

os.chdir('C:/Users/Ynche/Downloads/DBuster2/Agglomerated')
sensors_df = pd.read_csv("sensors_df.csv")

sensors_df.dtime = pd.to_datetime(sensors_df.dtime)
sensors_df['date'] = pd.to_datetime(sensors_df.dtime.dt.date)
# sensors_df['date'] = pd.to_datetime(sensors_df.date)
sensors_df['hour'] = sensors_df.dtime.dt.hour
sensors_df['weekday'] = sensors_df.dtime.dt.weekday
sensors_df['weekdayname'] = sensors_df.dtime.dt.weekday_name
sensors_final_dataset=sensors_df[~sensors_df.date.isin(pd.date_range(start='20150101', end='20170930'))]
sensors_final_dataset.to_csv('sensors_final_dataset.csv')
print(sensors_final_dataset.shape)
print(sensors_final_dataset.dtypes)