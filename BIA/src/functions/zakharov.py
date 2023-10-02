from typing import List

import numpy as np

from src.functions.base.function import Function

class Zakharov(Function):
    def calculate(self,
        params: List[float]) -> float:

        #first
        first: float = 0
        for xi in params:
            first += xi**2
        
        #second
        second: float = 0
        for i, xi in enumerate(params):
            second += 0.5 * (i + 1) * xi

        #summary
        ret: float = first + second**2 + second**4

        return ret