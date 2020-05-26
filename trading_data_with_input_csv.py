import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

#In this version, we'll read in the csv file that we created.
#We can also read in from other files like JSON and excel

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

#The head() is first six items, otherwise we'd have a huge list
print(df.head())

#You can index the dataframe object like a dictionary
#This allows us to print specific items
df['Adj Close'].plot()
plt.show()