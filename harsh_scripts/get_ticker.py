from nsetools import Nse
import quandl
import pandas as pd

nse = Nse()
stock_tickers= nse.get_stock_codes()
print(stock_tickers)

