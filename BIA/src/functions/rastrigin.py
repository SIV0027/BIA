import numpy as np
from src.functions.base.function import Function

class Rastrigin(Function):
    def calculate(self, params):
        d = len(params)

        #suma
        suma = 0
        for xi in params:
            suma += (xi**2 - 10 * np.cos(2 * np.pi * xi))

        #summary
        ret = 10 * d + suma

        return ret