import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

#df is a dataframe
#this is retrieving TSLA from yahoo for our given start and end times
#run this through terminal to 
df = web.DataReader('TSLA', 'yahoo', start, end)

#These commands print the data, but we'll comment them for the moment.
print(df.head())
print(df.tail())

#This command converts our data to a csv file
df.to_csv('tsla.csv')


