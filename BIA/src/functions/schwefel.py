from typing import List

import numpy as np

from src.functions.base.function import Function

class Schwefel(Function):
    def calculate(self,
        params: List[float]) -> float:

        d: int = len(params)

        #suma
        suma: float = 0
        for xi in params:
            suma += xi * np.sin(np.sqrt(np.abs(xi)))

        #summary
        ret: float = 418.9829 * d - suma

        return ret