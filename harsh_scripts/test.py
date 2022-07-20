from pandas_datareader import data as web
from datetime import datetime, timedelta
import talib
from nsetools import Nse
import pandas as pd

df = web.DataReader("TCS.NS", data_source = 'yahoo',
 					start = datetime.now() - timedelta(days = 100), end = datetime.now())

currentDate = datetime.now()
print(currentDate)
currentPrice=Nse().get_quote('tcs').get('lastPrice')

current = pd.DataFrame([[currentPrice]], columns=['Adj Close'], index=[currentDate])

df = pd.concat([df, pd.DataFrame(current)], ignore_index=False)

print(df)
ema_20 = talib.EMA(df['Adj Close'], timeperiod=20)
ema_50 = talib.EMA(df['Adj Close'], timeperiod=50)

print(ema_20-ema_50)