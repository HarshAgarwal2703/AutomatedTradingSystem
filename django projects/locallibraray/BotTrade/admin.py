from django.contrib import admin
from .models import Daylog,Portfolio,Watchlist,UserDb,OrderHistoryDb,PortfolioDb,WatchlistDb, CurrentPriceDb
# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Daylog)
admin.site.register(Watchlist)
admin.site.register(PortfolioDb)
admin.site.register(UserDb)
admin.site.register(WatchlistDb)
admin.site.register(OrderHistoryDb)
admin.site.register(CurrentPriceDb)