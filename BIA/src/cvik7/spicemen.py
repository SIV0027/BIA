import random

import numpy as np
import pandas as pd

from functions.base.function import Function
from functions.point.point import Point
from functions.point.reference_point import Reference_point

Intervals = list[tuple[float, float]]

class Spicemen:

    def __init__(self,
        function: Function,
        intervals: Intervals,
        step: float,
        path_length: float,
        prt: float
    ):
        
        self.function: Function = function
        self.intervals: Intervals = intervals
        self.step: float = step
        self.path_length: float = path_length
        self.prt: float = prt

        params: list[float] = list()
        for d in intervals:
            random_number: float = random.uniform(d[0], d[1])
            params.append(random_number)

        self.point: Reference_point = Point(func = self.function, params = params).create_reference()

    def get_point(self) -> Reference_point:

        return self.point

    def get_params(self) -> pd.Series:

        return pd.Series(self.point.get_params())

    def get_value(self) -> float:

        return self.point.get_value()

    def generate_perturbate_vector(self) -> pd.Series:

        perturbate_vector_params: list[float] = list()
        dimension: int = self.point.get_dimension()
        for _ in range(dimension):
            random_number: float = random.random()
            if random_number < self.prt:
                perturbate_vector_params.append(1)
            else:
                perturbate_vector_params.append(0)
        
        perturbate_vector: pd.Series = pd.Series(perturbate_vector_params)
        return perturbate_vector
    
    def migrate(self,
        leader_pos: pd.Series
    ) -> None:
        
        for _ in np.arange(0, self.path_length, self.step):
            move_point_params: pd.Series = (leader_pos - pd.Series(self.point.get_params())) 
            move_point_params *= self.step
            move_point_params *= self.generate_perturbate_vector()
            move_point_params += pd.Series(self.point.get_params())

            for index, dimension_item in enumerate(self.intervals):
                move_point_params[index] %= dimension_item[1]

            move_point: Reference_point = Point(self.function, move_point_params).create_reference()
            if move_point.get_value() < self.point.get_value():
                self.point = move_point