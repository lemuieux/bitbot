import ccxt
import pprint

bybit = ccxt.bybit()

def funding_rate_bybit():
    tick = bybit.fetch_ticker(symbol='BTC/USDT')
    tick_info = tick['info']
    return tick_info['funding_rate']
   
def predicted_funding_rate_bybit():
    tick = bybit.fetch_ticker(symbol='BTC/USDT')
    tick_info = tick['info']
    return tick_info['predicted_funding_rate']