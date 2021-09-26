from os import name
import pandas
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
z = cg.get_coins_markets(vs_currency='usd')
t = pandas.DataFrame(z, columns=['name', 'market_cap'])
print(t)