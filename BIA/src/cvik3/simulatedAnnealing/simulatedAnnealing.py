from typing import List, Tuple, cast

from src.search_methods.base.search_method import Search_method, Intervals

from src.commons.common import Common

from src.functions.base.function import Function
from src.functions.point.point import Point
from src.functions.point.reference_point import Reference_point

class SimulatedAnnealing(Search_method):
    def __init__(self,
        func: Function):
        
        super().__init__(func)

    #search minimum in function method by SimulatedAnnealing algorith
    def search(self,
            intervals: Intervals,
            **kwargs) -> Reference_point:
        
        #check if params ("**kwargs") is valid
        allowed_keys = ["t_0", "t_min", "alpha"]
        Common.check_kwargs("method search in SimulatedAnnealing class", allowed_keys, **kwargs)

        #assigment kwargs to params