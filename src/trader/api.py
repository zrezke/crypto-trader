import requests
import hmac
import hashlib
#  HMAC SHA256

class Api(Security):

    def __init__(self, secret_key):
        self.uri = "https://api.binance.com"
        self.secret_key = secret_key

    def trade(self, request):
        def sign():
            request.
            signiture = hmac.new(secret_key, total_params, hashlib.sha256).hexdigest()
            request()
        return sign

    def get_server_time(self):
        endpoint = self.uri + "api/v3/time"
        return requests.get(endpoint).json()

    @trade
    def make_new_order(self, params):
        endpoint = self.uri + "api/v3/order"
        print(signiture)


class Security:

    def __init__():
        pass
    
    def NONE():
        pass

    def TRADE():
        pass

    def USER_DATA():
        pass

    def USER_STREAM():
        pass

    def MARKET_DATA():
        pass
    