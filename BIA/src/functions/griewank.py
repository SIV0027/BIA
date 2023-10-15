from typing import List

import numpy as np

from functions.base.function import Function

class Griewank(Function):
    def calculate(self,
        params: List[float]) -> float:

        #first
        suma: float = 0
        for xi in params:
            suma += xi**2 / 4000

        #second
        product: float = 1
        for i, xi in enumerate(params):
            product *= np.cos(xi / np.sqrt((i + 1)))

        #summary
        ret: float = suma - product + 1

        return ret