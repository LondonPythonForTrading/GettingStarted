# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
#matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6


data = pd.read_csv('WIKI-AAPL.csv')
print(data.head())
print('\n Data Types:')
print(data.dtypes)


data['movingAvg20'] = data.filter(['Close']).rolling(window=20,center=False).mean()
data['movingAvg100'] = data.filter(['Close']).rolling(window=100,center=False).mean()
print(data.tail())

plt.figure(1)
plt.plot(data['Close'])
#plt.plot(data['movingAvg20'], color='r')
plt.plot(data['movingAvg100'], color='g')
plt.show()

