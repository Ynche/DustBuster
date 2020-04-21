import pandas as pd
import os

# Remark: the script requires files from previous step to be downloaded first.
# We create a csv where every row represents a daily summary for a sensor from the 317 sensors containing info about number of hourly observations.
os.chdir('C:/Users/Ynche/Downloads/DBuster')
summary_df = pd.DataFrame(columns=['sensor_id', 'date', 'observations','lon','lat'])
for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        df = pd.read_csv(file, sep=";")
        df['dtime'] = pd.to_datetime(df.timestamp)
        new_df = pd.DataFrame()
        new_df["P1"] = df.set_index('dtime').resample('H')['P1'].mean().round(2)# P1 hourly average
        new_df["P2"] = df.set_index('dtime').resample('H')['P2'].mean().round(2)# P2 hourly average
        summary_df = summary_df.append({'sensor_id': df.sensor_id[0], 'date': df.dtime.dt.date[0], 'observations': new_df.shape[0],'lon':df.lon[0],'lat':df.lat[0]}, ignore_index=True)
summary_df.to_csv('Agglomerated/summary.csv')