import pandas as pd
import json
import ast
import numpy as np
balanceDF=pd.read_csv(r"C:\Users\Harsh\Desktop\MP\harsh_scripts\balanceStmts.csv",na_filter=True, na_values='[]')
incomeDF=pd.read_csv(r"C:\Users\Harsh\Desktop\MP\harsh_scripts\incomeStmts.csv",na_filter=True, na_values='[]')

df_merged = pd.merge(balanceDF, incomeDF, on='SYMBOLS')
df_merged.dropna(inplace=True)
count = 0
roce_more=[]
def calROCE(i):
    global count
    balance=ast.literal_eval(i['balanceSheetHistoryQuarterly'])
    income=ast.literal_eval(i['incomeStatementHistoryQuarterly'])

    if balance is None:
        return np.NaN
    if income is None:
        return np.NaN
    if balance[0].get("2020-03-31") is None:
        tempBal=balance[1].get("2020-03-31")
    else:
        tempBal=balance[0].get("2020-03-31")
    if income[0].get("2020-03-31") is None:
        tempInc=income[1].get("2020-03-31")
    else:
        tempInc=income[0].get("2020-03-31")
    if tempBal is None:
        return np.NaN
    if tempInc is None:
        return np.NaN
    if tempBal.get("totalAssets") is None:
        return np.NaN
    if tempBal.get("totalCurrentLiabilities") is None:
        return np.NaN
    if tempInc.get("ebit") is None:
        return np.NaN
    assets=tempBal.get("totalAssets")
    liab=tempBal.get('totalCurrentLiabilities')
    ebit=tempInc.get("ebit")
    ROCE= (ebit/(assets-liab))*100
    if(ROCE>10):
        count+=1
        print(ROCE, i)
    return ROCE

# def calROE(i):
    # balance=ast.literal_eval(i['balanceSheetHistoryQuarterly'])
    # income=ast.literal_eval(i['incomeStatementHistoryQuarterly'])

    # if balance is None:
    #     return np.NaN
    # if income is None:
    #     return np.NaN

    # if balance[0] is None:
    #     return np.NaN
    # if balance[2] is None:
    #     print("b")
    #     return np.NaN
    # if income[0] is None:
    #     return np.NaN

    # if balance[0].get("2020-03-31") is None:
    #     tempBalNew=balance[1].get("2020-03-31")
    # else:
    #     tempBalNew=balance[0].get("2020-03-31")

    # if balance[2].get("2019-12-31") is None:
    #     tempBalPrev=balance[2].get("2019-12-31")
    # else:
    #     tempBalNew=balance[0].get("2020-03-31")

    # # if income[0].get("2020-03-31") is None:
    # #     tempInc=income[1].get("2020-03-31")
    # # else:
    # #     tempInc=income[0].get("2020-03-31")

    # # tempBalNew=balance[0].get("2020-06-30")

    # tempBalPrev=balance[2].get("2019-06-30")
    # tempInc=income[0].get("2020-03-31")

    # if tempBalNew is None:
    #     print("i")
    #     return np.NaN
    # if tempBalPrev is None:
    #     print("k")
    #     return np.NaN
    # if tempInc is None:
    #     return np.NaN
    # if tempBalNew.get("totalStockholderEquity") is None:
    #     return np.NaN
    # if tempBalPrev.get("totalStockholderEquity") is None:
    #     return np.NaN
    # if tempInc.get("netIncome") is None:
    #     return np.NaN

    # tot_equity_now =tempBalNew.get("totalStockholderEquity")
    # tot_equity_previous =tempBalPrev.get('totalStockholderEquity')
    # net_inc=tempInc.get("netIncome")
    # ROE= 2*net_inc/(tot_equity_now+tot_equity_previous)
    # print(ROE)
    # return ROE
   
roceList=[]

for i in range(len(df_merged)):
    roceList.append(calROCE((df_merged.iloc[i])))
    
print(count)
df_merged["ROCE"]=roceList

print(df_merged)
print(df_merged[df_merged.ROCE > 10])
print(df_merged[df_merged.ROCE > 10].SYMBOLS)

