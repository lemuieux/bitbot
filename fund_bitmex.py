import ccxt
import pprint

bitmex = ccxt.bitmex()

def funding_rate_bitmex():    
    tick = bitmex.fetch_ticker(symbol='BTC/USD')
    tick_info = tick['info']
    return tick_info['fundingRate']

def predicted_funding_rate_bitmex():
    tick = bitmex.fetch_ticker(symbol='BTC/USD')
    tick_info = tick['info']
    return tick_info['indicativeFundingRate']


# test
# print(funding_rate_bitmex())
# print(predicted_funding_rate_bitmex())
