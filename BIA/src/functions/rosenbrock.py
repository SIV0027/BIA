from typing import List

import numpy as np
from src.functions.base.function import Function

class Rosenbrock(Function):
    def calculate(self,
        params: List[float]) -> float:

        d: int = len(params)

        ret: float = 0
        for i in range(0, d - 1):
            xi: float = params[i]
            #first
            inner: float = params[i + 1] - xi**2
            first: float = 100 * inner**2

            #second
            second: float = (xi - 1)**2

            #summary
            ret += first + second

        return ret