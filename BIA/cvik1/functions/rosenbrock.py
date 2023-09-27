import numpy as np
from functions.base.function import Function

class Rosenbrock(Function):
    def calculate(self, params):
        d = len(params)

        ret = 0
        for i in range(0, d - 1):
            xi = params[i]
            #first
            inner = params[i + 1] - xi**2
            first = 100 * inner**2

            #second
            second = (xi - 1)**2

            #summary
            ret += first + second

        return ret