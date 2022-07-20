import pytrends
from pytrends.request import TrendReq
import pandas as pd

trending_terms = TrendReq(hl='en-IN', tz=-330)
keywords = ['share price','stock price']
trending_terms.build_payload(
      kw_list=keywords,
      cat=0,
      timeframe='now 1-d',
      geo='IN',
      gprop='')
# term_interest_over_time = trending_terms.interest_over_time()
# print(term_interest_over_time)

related_queries= trending_terms.related_queries()
top_queries=[]
rising_queries=[]
for key, value in related_queries.items():
    for k1, v1 in value.items():
        if(k1=="top"):
            top_queries.append(v1)
        elif(k1=="rising"):
            rising_queries.append(v1)
top_searched=pd.DataFrame(top_queries[1])
print(top_searched)
rising_searched=pd.DataFrame(rising_queries[1])
print(rising_searched)