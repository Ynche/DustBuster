import pandas as pd
import matplotlib.pyplot as plt
from datetime import date, timedelta
from mpl_toolkits.basemap import Basemap


def plot_observations_by_month(df:pd.DataFrame):
    """Function that takes a dataFrame as an argument and applies min/max latitude and longitude to select sensors in a specific rectangular area"""
    new_df =  df.groupby(pd.Grouper(key='date',freq='M'))["sensor_id"].count()
    new_df.plot(kind='bar',x='date',y=new_df[1])
    # plt.axvline('17-10', color='r', linestyle='dashed', linewidth=1)
    plt.xticks(range(len(new_df.index)),new_df.index.strftime("%Y-%m"))
    plt.xlabel("Month")
    plt.ylabel("Number of Daily Observations")
    return plt.show()


def plot_sensors_by_month(df:pd.DataFrame):
    new_df = df.groupby(pd.Grouper(key='date', freq='M'))["sensor_id"].nunique()
    new_df.plot(kind='bar', x='date', y=new_df[1])
    plt.xticks(range(len(new_df.index)), new_df.index.strftime("%Y-%m"))
    plt.xlabel("Month")
    plt.ylabel("Number of Sensors")
    return plt.show()

def hist_sensor_daily_observations(df:pd.DataFrame,bins,threshold:float,days:int):
    new_df = df.groupby('sensor_id')['observations'].count()
    plt.axvline(x=threshold * days, color='r', linestyle='dashed', linewidth=1)
    new_df.hist(bins=bins)
    plt.xlabel("Number of Daily Observations")
    plt.ylabel("Number of Sensors")
    return plt.show()

def hist_sensor_hourly_observations(df:pd.DataFrame,bins,threshold:float,days:int):
    new_df = df.groupby('sensor_id')['observations'].sum()
    plt.axvline(x=threshold * days *24, color='r', linestyle='dashed', linewidth=1)
    new_df.hist(bins = bins)
    plt.xlabel("Number of Hourly Observations")
    plt.ylabel("Number of Sensors")
    return plt.show()

def plot_map(df,map_name,final_sensor_list,remaining_sensor_list):
    sensors_plot_all = df.drop_duplicates(subset ="sensor_id", keep = 'first')
    sensors_plot_excluded = sensors_plot_all[~sensors_plot_all.sensor_id.isin(final_sensor_list)]
    sensors_plot_selected = sensors_plot_all[sensors_plot_all.sensor_id.isin(final_sensor_list)] # 29 selected sensors
    sensors_plot_excluded_after_oct2017 = sensors_plot_excluded[~sensors_plot_excluded.sensor_id.isin(remaining_sensor_list)]
    sensors_plot_excluded_before_oct2017 = sensors_plot_excluded[sensors_plot_excluded.sensor_id.isin(remaining_sensor_list)]# 50 excluded sensors
    m = Basemap(resolution='i',llcrnrlat = 42.64, llcrnrlon = 23.15, urcrnrlat = 42.75, urcrnrlon = 23.55,epsg=3035)
    plt.figure(figsize=[10,20])
    m.arcgisimage(service= map_name, xpixels = 7000, dpi=1000,verbose= True)
# m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 3500, dpi=500,verbose= True) #The street view oulines better the red sensors
    x, y = m(sensors_plot_selected.lon.tolist(), sensors_plot_selected.lat.tolist())
    z, v = m(sensors_plot_excluded_before_oct2017.lon.tolist(), sensors_plot_excluded_before_oct2017.lat.tolist())
    q, r = m(sensors_plot_excluded_after_oct2017.lon.tolist(), sensors_plot_excluded_after_oct2017.lat.tolist())
    m.plot(x, y, "o", markersize = 3, color = "red")
    m.plot(z, v, "o", markersize = 2, color = "blue")
    m.plot(q, r, "o", markersize = 2, color = "orange")
    plt.savefig("Sofia_{}.png".format(map_name),bbox_inches="tight")
    return plt.show()