import ccxt
import pprint

bitget = ccxt.bybit()

def funding_rate_bitget():
    tick = bitget.fetch_ticker(symbol='BTC/USD')
    tick_info = tick['info']
    return tick_info['funding_rate']

def predicted_funding_rate_bitget():
    tick = bitget.fetch_ticker(symbol='BTC/USD')
    tick_info = tick['info']
    return tick_info['predicted_funding_rate']

#test
print(funding_rate_bitget())
print(predicted_funding_rate_bitget())