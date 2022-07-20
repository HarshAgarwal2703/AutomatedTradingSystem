# https://github.com/samco-sdk/Python-SDK/blob/master/README.md
from django.shortcuts import render
from django.http import HttpResponse
from scripts.TradeBot import start
from .models import UserDb,WatchlistDb,PortfolioDb,OrderHistoryDb
#script imports
# from scripts.trading import *
# from scripts.algo import *
# from scripts.FindTrendingStocks import findTrendingStocks
# from datetime import datetime
# from datetime import date
# import pytz
# import time
# import csv
# import sqlite3
# import pandas as pd
# from BotTrade.models import Watchlist,Daylog
#----------

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
 
def home(request):
    return render(request,"home.html")

def startScript(request):
    user_Id=1
    start(user_Id)
    return render(request,"startScript.html")

def stopScript(request):
    return HttpResponse("Script Stoped")

def indexStock(request):
    return render(request,"index-stock-market.html")

def login(request):
    if request.method=="POST":
        name=request.POST["name"]
        password=request.POST["password"]
        try:
            user=UserDb.objects.get(name=name)
        except Exception:
            user=None
        # print("@@@@@@@@@@",user.values())
        if not user:
            return render(request,"login.html")
            # No user with that user name Found
            
        elif user.password==password:
            return render(request,"dashboard.html",{"name":name})
            #Login successfull

        return render(request,"dashboard.html",{"name":name,type:"Login"})
    else:
        return render(request,"login.html")


def register(request):

    if request.method=="POST":
        name=request.POST["name"]
        password=request.POST["password"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        print(mobile)
        if UserDb.objects.filter(email=email).exists() or UserDb.objects.filter(name=name).exists():
            print("user already exists")
            return render(request,"register.html")
            #User with email already exists
        else:
            UserDb.objects.create(name=name,password=password,email=email,mobile=0.0)
            return render(request,"login.html")

    else:
        return render(request,"register.html")

def initScript(request):
    return render(request,"initScript.html")


def dashboard(request):
    return render(request,"dashboard.html")


def startScriptForUser(request):
    #Starting the Script
    user_Id=1
    start(user_Id)
    
def stopScriptForUser(request):
    pass






