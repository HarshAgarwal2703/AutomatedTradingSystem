from pandas_datareader import data as pdr
import yfinance as yf
from yahoofinancials import YahooFinancials
import pandas as pd


# msft = yf.Ticker("MSFT")
# print(msft.info)
# print(msft.history)

# data = yf.download("INFY.NS", start="2020-01-01")
# print(data)

ticker = (YahooFinancials(["ARIHANT.NS", "RELIANCE.NS"]))
balance=ticker.get_financial_stmts('quarterly', 'balance')
income=ticker.get_financial_stmts('quarterly', 'income')
t=pd.read_csv(r"C:\Users\Harsh\Desktop\MP\t.csv")
t=pd.DataFrame(balance)

print(t)
t.to_csv('t.csv',  mode='a')
print(balance, "\n")
print("income", income, "\n")
if(balance != None):   
    temp=balance.get("balanceSheetHistory").get("ARIHANT.NS")[0].get("2020-03-31")
    ebit= ticker.get_ebit()
    print("\n ebit: ", ebit)
    assets=temp.get('totalAssets')
    print("\n asset: ", assets)
    liab=temp.get('totalCurrentLiabilities')
    print("\n liab: ", liab)
    ROCE=ebit/(assets-liab)*100
    print(ROCE)
else:
    print("Cannot be found")


