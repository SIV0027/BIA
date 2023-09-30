import numpy as np
from src.functions.base.function import Function

class Schwefel(Function):
    def calculate(self, params):
        d = len(params)

        #suma
        suma = 0
        for xi in params:
            suma += xi * np.sin(np.sqrt(np.abs(xi)))

        #summary
        ret = 418.9829 * d - suma

        return ret