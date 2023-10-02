from typing import List

from src.functions.base.function import Function

class Sphere(Function):
    def calculate(self,
        params: List[float]) -> float:
        
        ret: float = 0
        for xi in params:
            ret += xi**2

        return ret