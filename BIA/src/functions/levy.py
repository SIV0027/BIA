import numpy as np
from src.functions.base.function import Function

class Levy(Function):
    def w(self, i):
        ret = 1 + ((self.params[i] - 1) / 4)
        return ret

    def calculate(self, params):
        self.params = params
        d = len(params)

        #first
        first = np.sin(np.pi * self.w(0))**2

        #suma
        suma = 0
        for i in range(0, d - 1):
            xi = params[i]
            suma += (self.w(i) - 1)**2 * (1 + 10 * np.sin(np.pi * self.w(i) + 1)**2)

        #second
        second = (self.w(d - 1))**2 * (1 + np.sin(2 * np.pi * self.w(d - 1)**2))

        #summary
        ret = first + suma + second

        return ret