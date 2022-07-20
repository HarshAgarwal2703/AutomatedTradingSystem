import pandas as pd
import yfinance as yf

df = pd.read_csv(r"C:\Users\Harsh\Desktop\MP\tickerList.csv")

for i in df.index:
    
    print(df['SYMBOLS'][i])
    msft = yf.Ticker("MSFT")
