import numpy as np

from functions.point.point import Point
from functions.point.reference_point import Reference_point
from functions.base.function import Function

Intervals = list[tuple[float, float]]

class Firefly:

    def __init__(self, 
        intervals: Intervals
    ):

        self.intervals = intervals
        self.solution: np.ndarray = np.random.randn(len(intervals))
        self.check_bounds()

    def check_bounds(self):
        for dimension, bounds in enumerate(self.intervals):
            self.solution[dimension] %= bounds[1]

    def get_reference_point(self,
        function: Function
    ) -> Reference_point:

        refernce_point: Reference_point = Point(func = function,
                                                params = self.solution.tolist()).create_reference()
        return refernce_point

    def evaluate(self,
        function: Function
    ) -> float:
        
        value: float = function.calculate(self.solution.tolist())
        return value
    
    def move_to(self,
        partner: any,
        alpha: float            
    ) -> None:
        
        #decomposition to integral parts of new position calculating
        r: float = np.linalg.norm(self.solution - partner.solution)
        beta: float = 1 / (1 + r)
        #self new position calculating
        self.solution += beta + alpha * np.random.rand(2)
        self.check_bounds()
