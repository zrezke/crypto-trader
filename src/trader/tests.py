import api
import requests
import ta
import pandas as pd

BASE_URL = "https://api.binance.com/"
SERVER_TIME_ENDPOINT = BASE_URL + "api/v3/time"
CANDLE_DATA_ENDPOINT = BASE_URL + "api/v3/klines"
api_class = api.Api()
def api_security_test():
    params = "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"
    signiture = api_class.TRADE(params)
    print(signiture)

def api_order_test():
    kwargs = {
        "symbol": "ADABTC",
        "side": "BUY",
        "type": "LIMIT",
        "timestamp": api_class.get_server_time(),
        "quantity": 20,
        "price": '%.8f' % 0.00002360,
        "recvWindow": 5000,
        "timeInForce": "GTC" 
    }
    print(kwargs)
    resp = api_class.make_new_order(kwargs)
    print(resp)

def ta_df_test():
    serverTime = requests.get(SERVER_TIME_ENDPOINT).json()['serverTime']

    DATA_LIMIT = 518
    args = {
        "symbol": "ADABTC",
        "interval": "1m",
    }

    request = requests.get(CANDLE_DATA_ENDPOINT, params=args)
    data = request.json()
    data = [[float(val) for val in item] for item in data]

    df = pd.DataFrame(data, columns=["Timestamp", "Open", "High",
    "Low", "Close", "Volume", "close time", "qav", "n of trades", "tbbav", "tbqav", "ignore"])
    allIndicators = ta.add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume")
    print(allIndicators)
    allIndicators.to_csv('indicators.csv')
    '''
    rsi = ta.momentum.rsi(df["Close"], fillna=True)
    sRSI = ta.momentum.stochrsi(df["Close"])
    print(rsi.iloc[-1], sRSI.iloc[-1])
    '''
ta_df_test()