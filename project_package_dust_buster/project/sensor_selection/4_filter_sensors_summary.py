import pandas as pd
import os
from project.function_modules.functions_plot import plot_observations_by_month, plot_sensors_by_month



os.chdir('C:/Users/Ynche/Downloads/DBuster/Agglomerated')
raw_summary = pd.read_csv("summary.csv")
raw_summary['date'] = pd.to_datetime(raw_summary['date'])
print(raw_summary.groupby('date')["sensor_id"].count().head(1))# date 2017-02-22    1 - first sensor is Feb. 2017
# print(plot_observations_by_month(raw_summary))
# print(plot_sensors_by_month(raw_summary))

START_MONTH ='2017-10' #  establish a start date of the panel data study
summary = raw_summary.groupby(pd.Grouper(key='date',freq='M'))["sensor_id"].unique()
sensor_list = summary.filter(like=START_MONTH, axis=0).tolist() # narrow the list with sensors that have been in operation from Oct. 2017
print(sensor_list[0].size)  # 103

new_summary = raw_summary[raw_summary.sensor_id.isin(sensor_list[0])] # remove the sensors that started operation after Oct. 2017
new_summary = new_summary[~new_summary['date'].isin(pd.date_range(start='20150101', end='20170930'))]# remove observations before Oct. 2017

# print(plot_observations_by_month(new_summary))
# print(plot_sensors_by_month(new_summary))
# print(hist_sensor_observations(new_summary)) # max number of daily obs. = 821 days