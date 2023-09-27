import numpy as np
from function import Function

class Griewank(Function):
    def calculate(self, params):
        #first
        suma = 0
        for xi in params:
            suma += xi**2 / 4000

        #second
        product = 1
        for i, xi in enumerate(params):
            product *= np.cos(xi / np.sqrt((i + 1)))

        #summary
        ret = suma - product + 1

        return ret