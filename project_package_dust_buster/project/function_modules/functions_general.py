import pandas as pd

# Sofia city is better described as circular rather than a rectangular area. The filter is a rectangle.
def apply_location_criteria(df:pd.DataFrame,MAX_LAT,MIN_LAT,MAX_LON,MIN_LON) -> pd.DataFrame:
    """Function that takes a dataFrame as an argument and applies min/max latitude and longitude to select sensors in a specific rectangular area"""
    # For Sofia city the below coordinates are used
    # MAX_LAT = 42.75
    # MIN_LAT = 42.64
    # MAX_LON = 23.42
    # MIN_LON = 23.23
    selected = df[(df.lat <= MAX_LAT)&(df.lat >= MIN_LAT)&(df.lon <= MAX_LON)&(df.lon >= MIN_LON)]
    return selected

def select_sensors_with_daily_percent_completeness(df:pd.DataFrame,percent_complete_float:float,total_days:int) -> pd.DataFrame:
    new_df = df.groupby('sensor_id')['observations'].count()
    days_complete = round(total_days*percent_complete_float,0)
    reduced_df = new_df[new_df>=days_complete]
    remaining_df = new_df[new_df<days_complete]
    return reduced_df,remaining_df

def select_sensors_with_hourly_percent_completeness(df:pd,percent_complete_float:float,total_days:int)-> pd.DataFrame:
    new_df = df.groupby('sensor_id')['observations'].sum()
    hours_complete = round(total_days*24*percent_complete_float,0)
    reduced_df = new_df[new_df>=hours_complete]
    remaining_df = new_df[new_df<hours_complete]
    return reduced_df,remaining_df