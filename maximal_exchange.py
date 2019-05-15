import pandas as pd
import numpy as np
import datetime


raw_data = pd.read_csv('TRD.csv', names = ['Time', 'A', 'B', 'Exchange'])
for Exc in raw_data.Exchange.unique():
	part_data=raw_data.query('Exchange == @Exc')
	
Series=part_data['Time'].values
for index in range(0,len(Series)):
	Series[index]=datetime.datetime.strptime(Series[index],'%H:%M:%S.%f')
	
j=0
s = datetime.timedelta(seconds = 1)
for i in range(1, len(Series)):
	if (Series[i]-Series[j] < s):
		outj = j
		maximum = i-j+1
	else:
	j+=1
	
print('Максимальное количество сделок в течение одной секунды для биржи', 
Exc,'было между', Series[outj].time(), 'и', Series[outj+maximum-1].time(), 'и было продано', maximum)
