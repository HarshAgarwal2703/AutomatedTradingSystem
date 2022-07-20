from scripts.trading import *
from scripts.algo import *
from scripts.FindTrendingStocks import findTrendingStocks
from datetime import datetime
from datetime import date
import pytz
import time
import csv
import sqlite3
import pandas as pd
from BotTrade.models import Watchlist,Daylog,UserDb, WatchlistDb
from scripts.config import *

tz_NY = pytz.timezone('America/New_York')

def clearWatchlist():
	user_Id=userProfile["user_Id"]
	user_Object=userProfile["user_Object"]
	clear_watchlist= WatchlistDb.objects.filter(userObject=user_Object)
	if clear_watchlist.exists():
		WatchlistDb.objects.filter(userObject=user_Object).delete()
		print("successfully Cleared")
	else:
		print("Nothing to be Cleared")

def start(userID):
	tz_NY = pytz.timezone('America/New_York')
	userProfile["user_Id"]=userID
	userProfile["user_Object"]=UserDb.objects.get(id=userID)
	user_Id=userProfile["user_Id"]
	user_Object=userProfile["user_Object"]
	print("************************************************Script Start*******************************************************************")
	clearWatchlist()
	initPortfolio()
	findTrendingStocks()
	getWatchList()
	now = datetime.now(tz_NY)
	start = now.replace(hour=9, minute=30, second=0, microsecond=0)
	# checks time for stock market opening and runs the cycle function continuously
	while time.time()<time.time()+120:
		cycle()

# stores day's data into a SQL database
# con = sqlite3.connect('BotData.db')
# df = pd.read_csv('DayLog.csv')
# df.to_sql(str(date.today()), con, if_exists = 'append', index = False)

# resets files for the next day
# fObj = open('watchlist.csv', 'w')
# fObj.close()

#TODO Close Watclist database




