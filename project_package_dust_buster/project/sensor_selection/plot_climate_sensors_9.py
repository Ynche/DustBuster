import pandas as pd
from project.function_modules.functions_plot import plot_pollution
import os

os.chdir('C:/Users/Ynche/Downloads/DBuster2/Agglomerated')
sensors_climate = pd.read_csv('sensors_climate.csv')

print(plot_pollution(sensors_climate,'TEMP',3,-19,35,'gray','red','Temperature',"Level P1 - grey, P2 - red"))

print(plot_pollution(sensors_climate,'WIND',5,0,131,'darkgreen','springgreen',"Wind in m/s","Level P1 - blue, P2 - aqua"))

print(plot_pollution(sensors_climate,'PRESSURE',25,9911,10408,'plum','indigo',"Pressure in hPa","Level P1 - darkgreen, P2 - springgreen"))

print(plot_pollution(sensors_climate,'RAIN',2,0,35,'blue','aquamarine',"Precipitation in mm","Level P1 - aqua, P2 - blue"))

print(plot_pollution(sensors_climate,'SNOW',50,0,1033,'saddlebrown','gold',"Snow in mm equivalent","Level P1 - aqua, P2 - blue"))