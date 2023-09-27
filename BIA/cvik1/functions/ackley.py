import numpy as np
from functions.base.function import Function

class Ackley(Function):
    def calculate(self, params):
        d = len(params)

        #first
        sumx = 0
        for xi in params:
            sumx += xi**2

        sqrt = np.sqrt((1 / d) * sumx)
        exp_first = np.exp(-self.kwargs["b"] * sqrt)
        first = -self.kwargs["a"] * exp_first

        #second
        sumcos = 0
        for xi in params:
            sumcos += np.cos(self.kwargs["c"] * xi)

        second = np.exp((1 / d) * sumcos)

        #summary
        ret = first - second + self.kwargs["a"] + np.exp(1)

        return ret