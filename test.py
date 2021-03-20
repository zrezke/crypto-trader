import requests

BASE_URL = "https://api.binance.com/"
CANDLE_DATA_ENDPOINT = BASE_URL + "api/v3/klines"

args = {
    "symbol": "ETHBTC",
    "interval": "1h"
}

request = requests.get(CANDLE_DATA_ENDPOINT, params=args)
print(request.json())

'''
Here is this Bollinger Band® formula:

\begin{aligned} &\text{BOLU} = \text {MA} ( \text {TP}, n ) + m * \sigma [ \text {TP}, n ] \\ &\text{BOLD} = \text {MA} ( \text {TP}, n ) - m * \sigma [ \text {TP}, n ] \\ &\textbf{where:} \\ &\text {BOLU} = \text {Upper Bollinger Band} \\ &\text {BOLD} = \text {Lower Bollinger Band} \\ &\text {MA} = \text {Moving average} \\ &\text {TP (typical price)} = ( \text{High} + \text{Low} + \text{Close} ) \div 3 \\ &n = \text {Number of days in smoothing period (typically 20)} \\ &m = \text {Number of standard deviations (typically 2)} \\ &\sigma [ \text {TP}, n ] = \text {Standard Deviation over last } n \text{ periods of TP} \\ \end{aligned} 
​	  
BOLU=MA(TP,n)+m∗σ[TP,n]
BOLD=MA(TP,n)−m∗σ[TP,n]
where:
BOLU=Upper Bollinger Band
BOLD=Lower Bollinger Band
MA=Moving average
TP (typical price)=(High+Low+Close)÷3
n=Number of days in smoothing period (typically 20)
m=Number of standard deviations (typically 2)
σ[TP,n]=Standard Deviation over last n periods of TP
'''