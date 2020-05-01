import pandas as pd
import os
from datetime import date, timedelta

from project.function_modules.functions_general import select_sensors_with_hourly_percent_completeness, \
    select_sensors_with_daily_percent_completeness
from project.function_modules.functions_plot import plot_observations_by_month, plot_sensors_by_month, \
    hist_sensor_daily_observations, hist_sensor_hourly_observations, plot_map

START_MONTH ='2017-10' #  establish a start date of the panel data study
START_DAY = date(2017, 10, 1)
END_DAY = date(2019, 12, 31)
THRESHOLD = 0.95 #  establish a percent completeness of sensors' data
DELTA_TIME = END_DAY-START_DAY
DAYS = DELTA_TIME.days

os.chdir('C:/Users/Ynche/Downloads/DBuster2/Agglomerated')
raw_summary = pd.read_csv("summary.csv")
raw_summary['date'] = pd.to_datetime(raw_summary['date'])

print('The first observation \n{}'.format(raw_summary.groupby('date')["sensor_id"].count().head(1)))# date 2017-02-22    1 - first sensor is Feb. 2017
print('The total number of unique sensors is {}'.format(len(raw_summary.sensor_id.unique())))
print(plot_observations_by_month(raw_summary))
print(plot_sensors_by_month(raw_summary))

summary = raw_summary.groupby(pd.Grouper(key='date',freq='M'))["sensor_id"].unique()


sensor_list = summary.filter(like=f'{START_DAY.year}-{START_DAY.month}', axis=0).tolist() # narrow the list with sensors that have been in operation from Oct. 2017
print('Number of sensors {} in operation at START_DAY'.format(sensor_list[0].size))  # 103 have

new_summary = raw_summary[raw_summary.sensor_id.isin(sensor_list[0])] # remove the sensors that started operation after Oct. 2017
new_summary = new_summary[~new_summary['date'].isin(pd.date_range(start='20150101', end='20170930'))]# remove observations before Oct. 2017

print('Shape of unfiltered summary {}'.format(raw_summary.shape))
print('Shape of filtered summary {}'.format(new_summary.shape))
print(new_summary.head(5))
# print(plot_observations_by_month(new_summary))
# print(plot_sensors_by_month(new_summary))
print(hist_sensor_daily_observations(new_summary,30,THRESHOLD,DAYS)) # max number of daily obs. = 821 days, 102 sensors
print(hist_sensor_hourly_observations(new_summary,20,THRESHOLD,DAYS))

reduced_summary_hour,remaining_summary_hour =select_sensors_with_hourly_percent_completeness(new_summary,THRESHOLD,DAYS)

print('Number of sensors with hourly percent completeness {}'.format(reduced_summary_hour.shape))
print('Number of sensors excluded due to lack of completeness {}'.format(remaining_summary_hour.shape))

final_sensor_list = reduced_summary_hour.index.tolist() # we will work with 29 sensors
remaining_sensor_list = remaining_summary_hour.index.tolist()

print(plot_map(raw_summary,'ESRI_StreetMap_World_2D',final_sensor_list,remaining_sensor_list))
print(plot_map(raw_summary,'ESRI_Imagery_World_2D',final_sensor_list,remaining_sensor_list))
