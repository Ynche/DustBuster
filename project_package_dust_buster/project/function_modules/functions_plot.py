import pandas as pd
import matplotlib.pyplot as plt


def plot_observations_by_month(df:pd.DataFrame):
    """Function that takes a dataFrame as an argument and applies min/max latitude and longitude to select sensors in a specific rectangular area"""
    new_df =  df.groupby(pd.Grouper(key='date',freq='M'))["sensor_id"].count()
    new_df.plot(kind='bar',x='date',y=new_df[1])
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

def hist_sensor_observations(df:pd.DataFrame):
    new_df = df.groupby('sensor_id')['observations'].count()
    plt.hist(new_df,bins=20)
    plt.xlabel("Number of Daily Observations")
    plt.ylabel("Number of Sensors")
    return plt.show()