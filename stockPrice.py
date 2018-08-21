import os
import datetime as dt
from matplotlib import use, style
use('TkAgg')
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web
from pandas_datareader._utils import RemoteDataError

style.use('classic')
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()

def getPrice(ticker):


    df = web.DataReader(ticker, 'iex', start, end)
    df.reset_index(inplace=True)
    df.set_index("date", inplace=True)

    return df

def plotPrice(df):

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

    df['100ma'] = df['close'].rolling(window=100, min_periods=2).mean()
    #plt.plot(df.index, df['close'])
    ax1.plot(df.index, df['close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['volume'])
    print(8)
    print(5)
    plt.show()
    print(6)

df = getPrice('TSLA')
plotPrice(df)


