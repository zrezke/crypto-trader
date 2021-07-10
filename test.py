import requests
import pandas as pd
import ta
from ta.utils import dropna
from ta import add_all_ta_features

BASE_URL = "https://api.binance.com/"
SERVER_TIME_ENDPOINT = BASE_URL + "api/v3/time"
CANDLE_DATA_ENDPOINT = BASE_URL + "api/v3/klines"

serverTime = requests.get(SERVER_TIME_ENDPOINT).json()['serverTime']

DATA_LIMIT = 518
args = {
    "symbol": "ADABTC",
    "interval": "1m",
}

request = requests.get(CANDLE_DATA_ENDPOINT, params=args)
import TA
data = request.json()
def create_objects(data):
    return TA.Data(data)

data = [[float(val) for val in item] for item in data]

df = pd.DataFrame(data, columns=["Timestamp", "Open", "High",
 "Low", "Close", "Volume", "close time", "qav", "n of trades", "tbbav", "tbqav", "ignore"])
df.to_csv("lmao.csv")

rsi = ta.momentum.rsi(df["Close"], fillna=True)
sRSI = ta.momentum.stochrsi(df["Close"])
print(rsi.iloc[-1], sRSI.iloc[-1])
'''
df = add_all_ta_features(
    df, open="Open", high="High", low="Low", close="Close", volume="Volume")
'''
data_objs = [TA.Data(x) for x in data]

avg_gain = TA.average_gain(data_objs)
avg_loss = TA.average_loss(data_objs)

MA = TA.simple_moving_average([x.close_price for x in data_objs])
RSI = TA.rsi(avg_gain, avg_loss)

print("Avg. GAIn: ",avg_gain, "AVG. loss: ", avg_loss, "MA: ", MA, "RSI: ", RSI)

DEFAULT_RSI_PERIOD = 100
RSI_LOOKBACK_PERIOD =14

min_RSI = 101
max_RSI = 0