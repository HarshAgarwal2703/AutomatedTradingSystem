from nsetools import Nse
from pprint import pprint

nse = Nse()
print(nse)

q = nse.get_quote('infy') # it's ok to use both upper or lower case for codes.
pprint(q)
pprint(q.get("averagePrice"))
pprint(q.get("previousClose"))
pprint(q.get("pChange"))
pprint(q.get("change"))