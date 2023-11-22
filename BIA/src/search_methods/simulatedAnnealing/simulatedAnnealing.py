from typing import List, Tuple, cast

from search_methods.base.search_method import Search_method, Intervals

from commons.common import Common

import numpy as np
import math

from functions.base.function import Function
from functions.point.point import Point
from functions.point.reference_point import Reference_point

class SimulatedAnnealing(Search_method):
    def __init__(self,
        function: Function):
        
        super().__init__(function)

    #generate neighbour
    def generate_neighbour(self, 
        x: Reference_point,
        dim_avg_and_std_dev: Tuple[int, int]) -> Reference_point:

        dimension: int = x.get_dimension()

        params: List[float] = np.random.normal(x.get_params(),
                                               [0.1 for i in x.get_params()],
                                               dimension).tolist()
        solution: Point = Point(self.function, params)

        return solution.create_reference()

    #search minimum in function method by SimulatedAnnealing algorith
    def search(self,
            intervals: Intervals,
            **kwargs) -> Reference_point:
        
        #check if params ("**kwargs") is valid
        allowed_keys: List[str] = ["t_0", "t_min", "alpha"]
        Common.check_kwargs("method search in SimulatedAnnealing class", allowed_keys, **kwargs)

        #1. setting of control parameters - assigment kwargs to variables
        t_0: float = cast(float, kwargs.get(allowed_keys[0]))
        t_min: float = cast(float, kwargs.get(allowed_keys[1]))
        alpha: float = cast(float, kwargs.get("alpha"))

        t: float = t_0

        #2. generation of initial solution
        x: Reference_point = self.generate_random_solution(intervals)
        points: List[Reference_point] = []

        #3. main loop
        while t > t_min:
            x_1: Reference_point = self.generate_neighbour(x, (0, 5))
            if x_1.get_value() < x.get_value():
                points.append(x)
                x = x_1
            else:
                r: float = np.random.uniform()
                exponent: float = -(x_1.get_value() - x.get_value()) / t
                if r < math.e**exponent:
                    points.append(x)
                    x = x_1

            t *= alpha

        self.function.visualize(intervals, x, points)

        return x