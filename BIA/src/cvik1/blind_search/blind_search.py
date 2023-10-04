from typing import List, Tuple, cast

import random
import math
import numpy as np

from src.search_methods.base.search_method import Search_method

from src.commons.common import Common

from src.functions.base.function import Function
from src.functions.point.point import Point
from src.functions.point.reference_point import Reference_point

Intervals = List[Tuple[float, float]]

class Blind_search(Search_method):
    def __init__(self,
        function: Function):
        
        super().__init__(function)

    def generate_solution(self,
        intervals: Intervals) -> Reference_point:

        params: List[int] = []

        for interval in intervals:
            start: int = int(math.floor(interval[0]))
            end: int = int(math.floor(interval[1]))
            params.append(np.random.randint(start, end))

        ret = Point(self.function, params).create_reference()
        return ret

    def search(self,
        intervals: Intervals,
        **kwargs) -> Reference_point:

        allowed_keys: List[str] = ["count"]
        Common.check_kwargs("method search in Blind_search class", allowed_keys, **kwargs)

        count: int = cast(int, kwargs.get(allowed_keys[0]))

        #1. - generate random solution (which is currently best)
        best_solution: Reference_point = self.generate_solution(intervals)
        points: List[Reference_point] = []

        #2. - generate given count of solutions
        for i in range(count - 1):
            #2.a. - generate next solution
            random_solution: Reference_point = self.generate_solution(intervals)
            #2.b. - is random solution better than current best solution? 
            if random_solution.get_value() < best_solution.get_value():
                points.append(best_solution)
                best_solution = random_solution
            else:            
                points.append(random_solution)
        
        self.function.visualize(intervals, best_solution, points)

        return best_solution
