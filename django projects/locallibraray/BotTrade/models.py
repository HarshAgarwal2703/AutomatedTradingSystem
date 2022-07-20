from django.db import models

# #TODO 
# 1. USERS
# 	Name,Email,pswd,Mobile,Portolio(Foreign key),Buying Power(Money),Watchlist(Foreign key),OrderHistory(Fk)
# 2.Porfolio
# 	User_ID,StockName,Buying Price,Qty,Market Price, Profit/Loss
# 3.Watchlist
# 	User_ID,StockName
# 4.OrderHistory
# 	USer_ID, StockName,Action,Time,Qty,Price

# #TASKS
# 1.Models
# 2.Script
# 3.Views and UI

# cashInvested

#currentCash

class UserDb(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    mobile=models.FloatField(null=True)
    investedCash=models.FloatField(default=0.0)  #starting money you added in the app(static)
    portfolioWorthCash=models.FloatField(default=0.0) # money invested in stocks()
    currentLeftCash=models.FloatField(default=0.0)    # money left to buy more stocks
    netWorthCash=models.FloatField(default=0.0)       # currentCashLeft + portfolioWorthCash
    # portfolioId=models.ForeignKey(PortfolioDb, on_delete=models.CASCADE)
    # watchlistId=models.ForeignKey(WatchlistDb, on_delete=models.CASCADE)
    # orderHistoryId=models.ForeignKey(OrderHistoryDb, on_delete=models.CASCADE)

class CurrentPriceDb(models.Model):
    stockName=models.CharField(max_length=100)
    currentPrice=models.FloatField(null=True)
    prevClosePrice=models.FloatField(null=True)
    percentChange=models.FloatField(null=True)
    priceChange=models.FloatField(null=True)
    
class PortfolioDb(models.Model):
    userObject=models.ForeignKey(UserDb, on_delete=models.CASCADE)
    stockName=models.CharField(max_length=100)
    buyingPrice=models.FloatField()  
    quantity=models.IntegerField()
    currentPrice=models.ForeignKey(CurrentPriceDb, on_delete=models.CASCADE, null=True)
    stockWorth=models.FloatField(null=True) # current price * quantity
    profit=models.FloatField(null=True)   # stockWorth-buyingPrice*qauntity

class WatchlistDb(models.Model):
    userObject=models.ForeignKey(UserDb,on_delete=models.CASCADE)
    stockName=models.CharField(max_length=100)
    currentPrice=models.ForeignKey(CurrentPriceDb, on_delete=models.CASCADE, null=True)

   
class OrderHistoryDb(models.Model):
    userObject=models.ForeignKey(UserDb,on_delete=models.CASCADE)
    stockName=models.CharField(max_length=100)
    action=models.CharField(max_length=100)
    time=models.DateTimeField()
    quantity=models.IntegerField()
    price=models.FloatField()


    
    # Create your models here.
class Daylog(models.Model):
    symbol=models.CharField(max_length=100)
    time=models.DateTimeField()
    price=models.FloatField()
    upperBand=models.FloatField()
    lowerBand=models.FloatField()
    bandWidth=models.FloatField()
    rsi=models.FloatField()
    upperSlope=models.FloatField()
    realSlope=models.FloatField()
    lowerSlope=models.FloatField()
    upperI=models.FloatField()
    realI=models.FloatField()
    lowerI=models.FloatField()
    action=models.CharField(max_length=100)

class Portfolio(models.Model):
    symbol=models.CharField(max_length=100)
    quantity=models.FloatField()

class Watchlist(models.Model):
    symbol=models.CharField(max_length=100)






    
    
    
