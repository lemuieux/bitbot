import requests
import pandas as pd
import time
import webbrowser
import pyupbit
import json


# 15분 캔들
# url = "https://api.upbit.com/v1/candles/minutes/15"
# querystring = {"market":"KRW-BTC","count":"1"}
# headers = {"Accept": "application/json"}

#일 캔들
# url = "https://api.upbit.com/v1/candles/days"
# querystring = {"count":"1"}
# headers = {"Accept": "application/json"}

#response = requests.request("GET", url, headers=headers, params=querystring)

# 호가 정보
# url = "https://api.upbit.com/v1/orderbook"
# querystring = {"markets":"KRW-BTC"}
# headers = {"Accept": "application/json"}
# response = requests.request("GET", url, headers=headers, params=querystring)

# 현재가 정보
url = "https://api.upbit.com/v1/ticker"
querystring = {"markets":"KRW-AXS"}
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers, params=querystring)

# 출력
parsed = json.loads(response.text)
print(json.dumps(parsed, indent=4))

webbrowser.open("https://naver.com")

# a = 1 

# tickers = pyupbit.get_tickers()

# while True:
#     def rsiindex(symbol) :
#         url = "https://api.upbit.com/v1/candles/minutes/10"