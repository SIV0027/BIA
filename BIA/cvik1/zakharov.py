import numpy as np
from function import Function

class Zakharov(Function):
    def calculate(self, params):
        #first
        first = 0
        for xi in params:
            first += xi**2
        
        #second
        second = 0
        for i, xi in enumerate(params):
            second += 0.5 * (i + 1) * xi

        #summary
        ret = first + second**2 + second**4

        return ret