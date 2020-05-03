import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import os


os.chdir('C:/Users/Ynche/Downloads/DBuster2/Agglomerated')
climate = pd.read_csv('climate.csv')
sensors_final_dataset = pd.read_csv('sensors_final_dataset.csv')
sensors_final_dataset.dtime = pd.to_datetime(sensors_final_dataset.dtime)
climate.DATETIME = pd.to_datetime(climate.DATETIME)
sensors_climate = pd.merge(left=sensors_final_dataset,right=climate, how='left', left_on='dtime', right_on='DATETIME',)
sensors_climate.rename({'Unnamed: 0':'a'}, axis="columns", inplace=True)
sensors_climate.drop(["a"], axis=1, inplace=True)
# sensors_climate.drop(columns=['Unnamed: 0.1'])

sensors_climate.to_csv('sensors_climate.csv')


print('Shape of merged dataset {}'.format(sensors_climate.shape))
print('Types of merged dataset:\n{}'.format(sensors_climate.dtypes))
print('Description merged dataset:\n{}'.format(sensors_climate.describe()))
corr_matrix = sensors_climate.corr(method='pearson').round(2)


# sn.heatmap(corr_matrix, annot=True)
# print(plt.show())