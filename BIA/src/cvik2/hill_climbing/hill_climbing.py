from typing import List, Tuple, cast

from src.search_methods.base.search_method import Search_method

from src.commons.common import Common

import math
import random

from src.functions.base.function import Function
from src.functions.point.point import Point
from src.functions.point.reference_point import Reference_point

Intervals = List[Tuple[float, float]]

class Hill_climbing(Search_method):
    def __init__(self, 
        func: Function):

        super().__init__(func)

    
    #generate and return random solution (1.)
    def generate_random_solution(self,
        intervals: Intervals) -> Reference_point:
        
        params: List[int] = []
        for interval in intervals:
            params.append(random.randint(int(math.floor(interval[0])), int(math.floor(interval[1]))))

        solution: Point = Point(self.function, params)

        return solution.create_reference()


    #generate and return single neighbour (2.gen)
    def generate_single_neighbour(self, 
        actual_best: Reference_point,
        dim_avg_and_std_dev: Tuple[int, int]) -> Reference_point:

        params: List[int] = []
        for param in actual_best.get_params():
            params.append(int(param + random.gauss(dim_avg_and_std_dev[0], dim_avg_and_std_dev[1])))

        neighbour: Reference_point = Point(self.function, params).create_reference()
        return neighbour

    #generate and return neighbours (2.) (the best one and "others" for visualization)
    def generate_neighbours(self,
        actual_best: Reference_point,
        dim_avg_and_std_dev: Tuple[int, int],
        count_of_neighbours: int) -> Tuple[Reference_point, List[Reference_point]]:

        best_neighbour_params: List[int] = []

        neighbours: List[Reference_point] = [] #"other" neighbours
        #2.gen - generate first neighbour
        best_neighbour: Reference_point = self.generate_single_neighbour(actual_best, dim_avg_and_std_dev) #best neighbour

        #generate rest of neighbour (by "count_of_neighbours" argument)
        for i in range(count_of_neighbours - 1): # -1 because first neighbour is generated already (in 2.gen)
            #2.gen - generate next neighbour
            current_neighbour = self.generate_single_neighbour(actual_best, dim_avg_and_std_dev)
            if current_neighbour.get_value() < best_neighbour.get_value(): #is already generated one better than current best?
                neighbours.append(best_neighbour) #current best is just "other" neighbour now
                best_neighbour = current_neighbour #already generated is best one now
            else:
                neighbours.append(current_neighbour) #already generated is just "other" neighbour

        ret: Tuple[Reference_point, List[Reference_point]] = (best_neighbour, neighbours)
        return ret


    #search minimum of function in given list of intervals
    #(interval[from, to]: visualization range of dimension)
    def search(self,
        intervals: Intervals,
        **kwargs) -> Reference_point:

        allowed_keys: List[str] = ["dim_avg_and_std_dev", "count_of_neighbours", "count_of_itereations"]
        Common.check_kwargs("method search in Hill_climbing class", allowed_keys, **kwargs)

        dim_avg_and_std_dev: Tuple[int, int] = cast(Tuple[int, int], kwargs.get(allowed_keys[0]))
        count_of_neighbours: int = cast(int, kwargs.get(allowed_keys[1]))
        count_of_itereations: int = cast(int, kwargs.get(allowed_keys[2]))

        neighbours: List[Reference_point] = []
        #1. - generate random solution
        best_solution: Reference_point = self.generate_random_solution(intervals)
        #2. - generate neighbours - the best of (by iterations)
        for i in range(count_of_itereations):
            current_local_solution, others_neighbours = self.generate_neighbours(best_solution, 
                                                                                 dim_avg_and_std_dev,
                                                                                 count_of_neighbours)
            neighbours += others_neighbours
            #3. - is neighbour better than current best solution?
            if current_local_solution.get_value() <= best_solution.get_value():
                neighbours.append(best_solution)
                best_solution = current_local_solution

        self.function.visualize(intervals, best_solution, neighbours)

        return best_solution