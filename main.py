import rsi_upbit
import rsi_bybit
import rsi_binance
import fund_bybit
import fund_binance
import fund_bitmex
import fear_greed

while True:
    print("----------------------------------")
    print("rsi_upbit(15) : " + str(rsi_upbit.rsi_upbit(15)))
    print("rsi_bybit(15) : " + str(rsi_bybit.rsi_bybit(15)))
    print("rsi_binance(15) : " + str(rsi_binance.rsi_binance('15m')))
    print("----------------------------------")
    print("rsi_upbit(60) : " + str(rsi_upbit.rsi_upbit(60)))
    print("rsi_bybit(60) : " + str(rsi_bybit.rsi_bybit(60)))
    print("rsi_binanace(60) : " + str(rsi_binance.rsi_binance('1h')))
    print("----------------------------------")
    print("rsi_upbit(240) : " + str(rsi_upbit.rsi_upbit(240)))
    print("rsi_bybit(240) : " + str(rsi_bybit.rsi_bybit(240)))
    print("rsi_binance(240) : " + str(rsi_binance.rsi_binance('4h')))
    print("----------------------------------")
    print("fund_bybit : " + str(fund_bybit.funding_rate_bybit()))
    print("fund_binance : " + str(fund_binance.funding_rate_binance()))
    print("fund_bitmex : " + str(fund_bitmex.funding_rate_bitmex()))
    print("----------------------------------")
    print("p_fund_bybit : " +str(fund_bybit.predicted_funding_rate_bybit()))
    print("p_fund_bitmex : " +str(fund_bitmex.predicted_funding_rate_bitmex()))
    print("----------------------------------")
    print("fear_greed(twodaysago) : " + str(fear_greed.fear_twodaysago()))
    print("fear_greed(yesterday) : " + str(fear_greed.fear_yester()))
    print("fear_greed(today) : " + str(fear_greed.fear_day()))