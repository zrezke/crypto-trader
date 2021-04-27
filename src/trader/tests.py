import api
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

api_order_test()