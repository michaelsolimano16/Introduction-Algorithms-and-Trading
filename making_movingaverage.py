import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')


df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

#generate a 100 day moving average field by taking mean of 100 previous dates
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#get rid of any points (specifically, the early ones) without enough data to generate 100ma
df.dropna(inplace=True)

#for multiple graphs in matplotlib, we need multiple subplots

#first param is graph size (here it's 6rows x 1column)
#Second param is starting point
#rowspan is how many rows it will span
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

#Here, the x values are date. this is accessed by df.index.
#y val is adjusted close

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])

#This is another plot, but does it with bars
ax2.bar(df.index, df['Volume'])

plt.show()