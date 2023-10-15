from typing import List, Tuple

import numpy as np

from functions.base.function import Function

class Ackley(Function):
    def __init__(self, **kwargs):
        super().__init__(["a", "b", "c"], **kwargs)

        self.a = kwargs.get("a")
        self.b = kwargs.get("b")
        self.c = kwargs.get("c")

    def calculate(self, 
        params: List[float]) -> float:

        d: int = len(params)

        #first
        sumx: float = 0
        for xi in params:
            sumx += xi**2

        sqrt: float = np.sqrt((1 / d) * sumx)
        exp_first: float = np.exp(-self.b * sqrt)
        first: float = -self.a * exp_first

        #second
        sumcos: float = 0
        for xi in params:
            sumcos += np.cos(self.c * xi)

        second: float = np.exp((1 / d) * sumcos)

        #summary
        ret: float = first - second + self.a + np.exp(1)

        return ret