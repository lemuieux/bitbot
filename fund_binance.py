import ccxt
import pprint

def funding_rate_binance():
    binance = ccxt.binance({'options': {
        'defaultType': 'future',
    }})    

    fund = binance.fetch_funding_rate(symbol='BTC/USDT')
    return fund['interestRate']

# test
# fund_binance()