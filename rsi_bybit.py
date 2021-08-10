from pybit import HTTP
import requests
import pandas as pd
import time
from datetime import datetime
import calendar
import json
import pprint
import os

# 여기부터 ~ 
# print(os.getcwd())
f = open("bitbot/key/bybit_key.txt", 'r')
apiKey = f.readline()
apiSecret = f.readline()
f.close()

session = HTTP(
    endpoint='https://api.bybit.com', 
    api_key=apiKey,
    api_secret=apiSecret
)

def rsi_bybit(itv, symbol='BTCUSD'):
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.utctimetuple())
    since = unixtime-itv*60*200;
    response=session.query_kline(symbol='BTCUSD',interval=str(itv),**{'from':since})['result']
    df = pd.DataFrame(response)
    # df=df.reindex(index=df.index[::-1]).reset_index()
    rsi=rsi_calc(df,14).iloc[-1]
    return rsi

def rsi_calc(ohlc: pd.DataFrame, period: int = 14):
    ohlc = ohlc['close'].astype(float)
    delta = ohlc.diff()
    gains, declines = delta.copy(), delta.copy()
    gains[gains < 0] = 0
    declines[declines > 0] = 0

    _gain = gains.ewm(com=(period-1), min_periods=period).mean()
    _loss = declines.abs().ewm(com=(period-1), min_periods=period).mean()

    RS = _gain / _loss
    return pd.Series(100-(100/(1+RS)), name="RSI")

# test
# while True:
#     rsi_bybit(15)
#     rsi_bybit(60)    
#     rsi_bybit(240)

#     time.sleep(1)