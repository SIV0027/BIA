from typing import List
from abc import ABC, abstractmethod

from functions.base.function import Function
from functions.point.reference_point import Reference_point

import math
import numpy as np

from search_methods.base.intervals import Intervals

from functions.base.function import Function
from functions.point.point import Point
from functions.point.reference_point import Reference_point

class Search_method(ABC):
    def __init__(self,
        function: Function):
        
        self.function: Function = function

    #method to generate random solution in given intervals
    def generate_random_solution(self,
        intervals: Intervals) -> Reference_point:

        params: List[float] = np.random.uniform([coord[0] for coord in intervals],
                                                [coord[1] for coord in intervals],
                                                len(intervals)).tolist()       
        solution: Point = Point(self.function, params)

        return solution.create_reference()

    #abstract method of searching minimum in function for overriding
    @abstractmethod
    def search(self, 
        intervals: Intervals,
        **kwargs) -> Reference_point:
        pass