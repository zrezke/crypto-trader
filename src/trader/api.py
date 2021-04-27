import requests
import hmac
import hashlib
import json
#  HMAC SHA256

class Security(object):

    def __init__(self):
        # For security reasons I have my keys stored locally :)
        with open("secret.json") as json_file:
            secrets = json.load(json_file)

        self.secret_key = secrets["secret_key"].encode('utf-8')
        self.api_key = secrets["api_key"]

    def NONE(self):
        """NONE	Endpoint can be accessed freely."""
        return None

    def TRADE(self, total_params):
        """TRADE Endpoint requires sending a valid API-Key and signature."""
        headers = {"X-MBX-APIKEY": self.api_key}
        signiture = self._sign(total_params)
        params = f"{total_params}&signature={signiture}"
        return (headers, params)

    def USER_DATA(self, total_params):
        """USER_DATA Endpoint requires sending a valid API-Key and signature."""
        headers = {"X-MBX-APIKEY": self.api_key}
        signiture = self._sign(total_params)
        params = f"{total_params}&signature={signiture}"
        return (headers, params)

    def USER_STREAM(self, total_params):
        headers = {"X-MBX-APIKEY": self.api_key}
        return headers

    def MARKET_DATA(self, total_params):
        """MARKET_DATA Endpoint requires sending a valid API-Key."""
        headers = {"X-MBX-APIKEY": self.api_key}
        return headers
    
    def _sign(self, total_params):
        return hmac.new(self.secret_key, total_params.encode('utf-8'), hashlib.sha256).hexdigest()


class Api(Security):

    def __init__(self):
        super().__init__()
        self.uri = "https://api.binance.com"

    def get_server_time(self) -> int:
        endpoint = self.uri + "/api/v3/time"
        return requests.get(endpoint).json()["serverTime"]

    def get_klines(self, params):
        endpoint = self.uri + "/api/v3/klines"
        return requests.get(endpoint, params=params).json()

    def make_new_order(self, params):
        """
        params: {
            symbol: `STRING` @required,
            side: `ENUM` @required,
            type: `ENUM` @required,
            timestamp: `LONG` @required,
            price: `DECIMAL` @required,
            quantity: `DECIMAL` @required,
            timeInForce: `STRING` @required,
            [recvWindow] `INT` @recomended recomended val: 5000,
            [newClientOrderId]: `STRING` @recomended,
        }
        """
        endpoint = self.uri + "/api/v3/order/test"
        security = self.TRADE(self._stringifyParams(params))
        headers = security[0]
        _params = security[1]
        return requests.post(endpoint, params=_params, headers=headers).json()

    def _stringifyParams(self, params):
        string = ""
        for key, val in params.items():
            string += f"{key}={val}&"
        return string.rstrip("&")