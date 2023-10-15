from typing import List, Union

from functions.base.function import Function
from functions.point.reference_point import Reference_point

class Point:
    def __init__(self, func: Function, params: List[float]):
        self.params: List[float] = params
        self.value: float = func.calculate(self.params)

    def create_reference(self) -> Reference_point:
        return Reference_point(self.params, self.value)