import pandas as pd
from datetime import date, timedelta
import wget

# Remark: the script requires large free space on disk and and is highly time consuming.
# At the end of the execution all csv files for the selected sensors and predefined period are downloaded in the destination folder.
all_sensors = pd.read_csv('all_sensors.csv')
sensor_list = all_sensors.sensor_id.tolist() # list of 352 sensors in Sofia
start_date = date(2015, 10, 1)   # start date of the Luftdaten project
end_date = date(2019, 12, 31)   # end date (the study has been conducted in Jan. 2020, therefore the day can be extended)
delta = end_date - start_date       # as timedelta
destination_folder = "C:/DBuster2/"
for day in range(delta.days + 1): # download all csv files for the selected sensors and selected period
    day = start_date + timedelta(days=day)
    for sensor in sensor_list:
        # the naming convention of the luftdaten archive includes the date and sensor id in the name of the url
        urlfolder = "http://archive.luftdaten.info/" + str(day) + "/" + str(day) + "_sds011_sensor_"+str(sensor)+".csv"
        destination = destination_folder + str(day) + "_sds011_sensor_"+str(sensor)+".csv"
        try:
            wget.download(urlfolder, destination)
        except:
            continue