from typing import List

import numpy as np

from src.functions.base.function import Function

class Michalewicz(Function):
    def __init__(self, **kwargs):
        super().__init__(["m"], **kwargs)

        self.m: int = kwargs.get("m")

    def calculate(self,
        params: List[float]) -> float:

        #suma
        suma: float = 0
        for i, xi in enumerate(params):
                suma += np.sin(xi) * np.sin(((i + 1) * xi**2) / np.pi)**(2 * self.m)

        #summary
        ret: float = -suma

        return ret