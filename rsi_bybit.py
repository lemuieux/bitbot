from pybit import HTTP
import requests
import pandas as pd
import time
from datetime import datetime
import calendar
import json

apiKey = ""
apiSecret = ""

session = HTTP(
    endpoint='https://api.bybit.com', 
    api_key=apiKey,
    api_secret=apiSecret
)

def rsi_calc(ohlc: pd.DataFrame, period: int = 14):
    delta = ohlc.diff()
    gains, declines = delta.copy(), delta.copy()
    gains[gains < 0] = 0
    declines[declines > 0] = 0

    _gain = gains.ewm(com=(period-1), min_periods=period).mean()
    _loss = declines.abs().ewm(com=(period-1), min_periods=period).mean()

    RS = _gain / _loss
    return pd.Series(100-(100/(1+RS)), name="RSI")


# test
while True:
    now = datetime.utcnow()
    unixtime = calendar.timegm(now.utctimetuple())
    since = unixtime - 60 * 60 *24*200
    response=session.query_kline(symbol='BTCUSD',interval="15",**{'from':since})['result']
    
    df = pd.DataFrame(response)
    
    df=df.reindex(index=df.index[::-1]).reset_index()

    rsi=rsi_calc(df,14).iloc[-1]

    #print(rsi)

    time.sleep(1)

