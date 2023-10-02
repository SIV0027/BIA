from typing import List, Tuple

import numpy as np

from src.functions.base.function import Function

class Rastrigin(Function):
    def calculate(self, 
        params: List[float]) -> float:

        d: int = len(params)

        #suma
        suma: float = 0
        for xi in params:
            suma += (xi**2 - 10 * np.cos(2 * np.pi * xi))

        #summary
        ret: float = 10 * d + suma

        return ret