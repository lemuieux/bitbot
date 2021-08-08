import ccxt
import pprint

def fund_binance():
    binance = ccxt.binance({'options': {
        'defaultType': 'future',
    }})    

    fund = binance.fetch_funding_rate(symbol='BTC/USDT')
    pprint.pprint(fund)
    return fund['interestRate']

# test
# fund_binance()