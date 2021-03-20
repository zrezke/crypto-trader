import math

class TA:
    def __init__(self, data):
        self.data = data
        self.closePriceSum = sum(map(lambda x: float(x[4]), data))
        self.numberOfPeriods = len(data)
    
    def simple_moving_average(self):
        return self.closePriceSum / self.numberOfPeriods

    def stoch_relative_strength_index(self):
        pass
    
    def boiler_bands(self):
        pass

    def moving_average_convergence_divergence(self):
        pass
