from typing import List, Tuple
from abc import ABC, abstractmethod

from src.functions.base.function import Function
from src.functions.point.reference_point import Reference_point

Intervals = List[Tuple[float, float]]

class Search_method(ABC):
    def __init__(self,
        function: Function):
        
        self.function: Function = function

    #abstract method of searching minimum in function for overriding
    @abstractmethod
    def search(self, 
        intervals: Intervals,
        **kwargs) -> Reference_point:
        pass