from typing import List, Tuple
from abc import ABC, abstractmethod

from src.functions.base.function import Function
from src.functions.point.reference_point import Reference_point

class Search_method(ABC):
    def __init__(self,
        function: Function):
        
        self.function: Function = function

    #abstract method of searching minimum in function for overriding
    @abstractmethod
    def search(self, 
        intervals: List[Tuple[float, float]],
        **kwargs) -> Reference_point:
        pass