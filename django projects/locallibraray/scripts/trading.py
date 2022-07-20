import pandas_datareader.data as web
import pandas as pd
from scripts.FindTrendingStocks import findTrendingStocks
from scripts.algo import decide
from datetime import datetime
import alpaca_trade_api as tradeapi
import requests
import json
from scripts.config import *
from scripts.algo import *
from scripts.TradeBot import *	
import os
import time
import csv
from pandas_datareader._utils import RemoteDataError
from BotTrade.models import Watchlist, Portfolio, WatchlistDb
 
# alpaca api information, used for requests
BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID' : API_KEY, 'APCA-API-SECRET-KEY' : SECRET_KEY}

# returns json of information on the account, like equity, buying power, etc.
def getAccountInfo():
	r = requests.get(ACCOUNT_URL, headers = HEADERS)
	return json.loads(r.content)

# creates an order for either buy or sell
def create_order(symbol, qty, side, type, time_in_force):
	data = {
		'symbol' : symbol,
		'qty' : qty,
		'side' : side,
		'type' : type,
		'time_in_force' : time_in_force
	}
	try:
		r = requests.post(ORDERS_URL, json = data, headers = HEADERS)
		response = json.loads(r.content)
		return json.loads(r.content)
	except NameError as e:
		print(e)

# get stocks on the watchlist and portfolio and save them in a set to determine
# which stocks to watch		
def getWatchList():
	user_Object=userProfile["user_Object"]
	trending = []
	trending_dic = WatchlistDb.objects.filter(userObject=user_Object)
	# fObj = open('watchlist.csv')
	for line in trending_dic:
		trending.append(line.stockName)
		print(line.stockName)
	watchlist = list(portfolio.keys()) + trending
	watchlist = set(watchlist)
	return watchlist

# updates the portfolio.csv file after transactions
def updatePortfolio(stock_name, quantity ,buying_price):
	# fObj = open('portfolio.csv', 'w')
	user_Object=userProfile["user_Object"]
	try :
		portfolioObject=PortfolioDb.objects.get(userObject=user_Object, stockName=stock_name)
		if portfolioObject :
			newQuantity=portfolioObject.quantity+quantity
			newPrice=(portfolioObject.buyingPrice*portfolioObject.quantity+buying_price*quantity)/newQuantity
			portfolioObject.quantity=newQuantity
			portfolioObject.buyingPrice=newPrice
			portfolioObject.save()
			# portfolioObject.update(stockName="ABC", quantity=newQuantity, buyingPrice=newPrice)
		else:
			PortfolioDb.objects.create(userObject=user_Object, stockName=stock_name, quantity=quantity, buyingPrice=buying_price)
	except Exception as e:
		print(e)

def deletePortfolio(stock_name):
	user_Object=userProfile["user_Object"]
	try :
		portfolioObject=PortfolioDb.objects.get(userObject=user_Object, stockName=stock_name)
		portfolioObject.delete()
	except Exception as e:
		print(e)
	# for key in portfolio:
	# 	PortfolioDb.objects.create(userObject=user_Object, stockName=key, quantity=portfolio[key], buyingPrice=buying_price)
	# for key in portfolio:
	# 	fObj.write(str(key) + ',' + str(portfolio[key]) + '\n')
	# fObj.close()

# cycle function that will repeat (loop), gets stock data and decides what to do
def cycle():
	# watchlist = Watchlist.objects.all()
	watchlist = getWatchList()
	for symbol in watchlist:
		try:
			move=decide(symbol)
			# move = decide(symbol)
			if move == 'sell':
				create_order(symbol, portfolio[symbol], 'sell', 'market', 'gtc')
				print('Sold ' + symbol + ' at ' + str(getPrice(symbol)))
				# TODO delete symbol from portfolio
				del portfolio[symbol]
				deletePortfolio(stock_name)
				# updatePortfolio(0)
			elif move == 'buy':
				if float(getAccountInfo()['buying_power']) < 3000:
					continue;
				create_order(symbol, 3000 // getPrice(symbol), 'buy', 'market', 'gtc')
				print('Bought ' + symbol + ' at ' + str(getPrice(symbol)))
				# portfolio[symbol] = 3000 // getPrice(symbol)
				# updatePortfolio()
				quantity= 3000 // getPrice(symbol)
				buying_price=getPrice(symbol)
				updatePortfolio(symbol, quantity, buying_price)
			else:
				continue;
		except RemoteDataError as e:
			print(e)
		except KeyError as a:
			print(a)

