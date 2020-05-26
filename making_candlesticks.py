import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')


df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

#Below will resample the data to a metric of our choosing. (Here, 10 day mean)
# ohlc() is open, high, low, close

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

# candlestick_ohlc wants date (in mdate), then ohlc.

df_ohlc.reset_index(inplace=True)

#Convert dates to mdates
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)


ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)

#Convert back to readable dates on our graph
ax1.x_axisdate()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()

#Here, the x values are date. this is accessed by df.index.
#y val is adjusted close

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])

#This is another plot, but does it with bars
ax2.bar(df.index, df['Volume'])

plt.show()