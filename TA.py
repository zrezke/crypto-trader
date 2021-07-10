import math

class Data:
    def __init__(self, data):
        self.data = data

    @property
    def open_time(self):
        return self.data[0]

    @property
    def open_price(self):
        return float(self.data[1])
    
    @property
    def high(self):
        return float(self.data[2])
    
    @property
    def low(self):
        return float(self.data[3])
        
    @property
    def close_price(self):
        return float(self.data[4])
    
    @property
    def volume(self):
        return float(self.data[5])
    
    @property
    def diff(self):
        return self.close_price - self.open_price

    @property
    def gain(self):
        return self.diff if self.diff > 0 else 0
    
    @property
    def loss(self):
        return abs(self.diff) if self.diff < 0 else 0
    
def average_gain(data):
    gains = [x.gain for x in data]
    sma = simple_moving_average(gains)
    return sma

def average_loss(data):
    losses = [x.loss for x in data]
    sma = simple_moving_average(losses)
    return sma

def relative_strength(avg_gain, avg_loss):
    return avg_gain/avg_loss

def simple_moving_average(data):
    return sum(data)/len(data)

def exponential_moving_average(data):
    N = len(data)
    alpha = 2 / ( N + 1 )


def rsi(avg_gain, avg_loss):
    RS = relative_strength(avg_gain, avg_loss)
    print(RS, "LMAO")
    return  100 - 100/(1 + RS)