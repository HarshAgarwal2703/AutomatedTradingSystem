from yahoofinancials import YahooFinancials
import pandas as pd
import json

tickerDF= pd.read_csv(r"C:\Users\Harsh\Desktop\MP\alltickers.csv")
tickerList= tickerDF["SYMBOL.NS"].tolist()
batchList=[]
for i in range(11):
    batchList.append(tickerList[0+(i*167):167+(i*167)])

bactchNO=10
print(batchList[bactchNO])
ticker = (YahooFinancials(batchList[bactchNO]))

balanceStmts=ticker.get_financial_stmts('quarterly', 'balance')
balanceDF=pd.DataFrame((balanceStmts))


incomeStmts=ticker.get_financial_stmts('quarterly', 'income')
incomeDF=pd.DataFrame((incomeStmts))

balanceDF.to_csv('balanceStmts.csv',  mode='a')

incomeDF.to_csv('incomeStmts.csv',  mode='a')

print(incomeDF)
print(balanceDF)

