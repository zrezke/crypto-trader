import ta
import pandas as pd


def build(kline_data) -> pd.DataFrame:
    """
    :param: kline_data `json`
    """
    data = [[float(val) for val in item] for item in kline_data]

    df = pd.DataFrame(data, columns=["Timestamp", "Open", "High",
    "Low", "Close", "Volume", "close time", "qav", "n of trades", "tbbav", "tbqav", "ignore"])
    return ta.add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume")
