from typing import List, Tuple

import random

from src.functions.base.function import Function

class Hill_climbing:
    def __init__(self, 
        func: Function):

        self.func: Function = func

    #generate and return list of neighbours
    #(neighbour[x1, x2, x3, ...]: list of its corrds (len(coords): count of dimensions))
    def generate_neigbours(self,
        dims_avgs_and_std_devs: List[Tuple[float, float]],
        count_of_neighbours: int) -> List[List[int]]:

        ret: List[List[int]]

        for _ in range(count_of_neighbours):
            pass

    #search minimum of function in given list of intervals
    #(interval[from, to]: visualization range of dimension)
    def search(self,
        intervals: List[Tuple[float, float]]) -> None:

        

        #self.generate_neigbour()
        
        self.func.visualize(x1From, x1To, x2From, x2To, [], [0, 0, 0])