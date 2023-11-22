import random

import pandas as pd

from functions.base.function import Function
from functions.point.point import Point
from functions.point.reference_point import Reference_point

Intervals = list[tuple[float, float]]

class Particle:

    def __init__(self,
    function: Function,
    inital_coords: list[float],
    initial_speed: list[float]):

        self.function: Function = function        
        self.position: Reference_point = Point(self.function, inital_coords).create_reference()
        self.speed: list[float] = initial_speed

        self.pBest: Reference_point = self.position

    def calculate_speed(self,
    c1: int,
    c2: int,
    gBest: Reference_point,
    v_max: float) -> None:

        speed_v: pd.Series = pd.Series(self.speed) 
        pBest_v: pd.Series = pd.Series(self.pBest.get_params())
        position_v: pd.Series = pd.Series(self.position.get_params())
        gBest_v: pd.Series = pd.Series(gBest.get_params())

        speed_v = speed_v + c1 * random.uniform(0, 1) * (pBest_v - position_v)
        speed_v += c2 * random.uniform(0, 1) * (gBest_v - position_v)
        for index, item in enumerate(self.speed):
            if item > v_max:
                self.speed[index] = v_max

    def move(self,
    intervals: Intervals) -> None:
        
        position: pd.Series = pd.Series(self.position.get_params())
        speed: pd.Series = pd.Series(self.speed)

        position += speed
        position_list: list[float] = position.values.tolist()
        for index, item in enumerate(position_list):
            position_list[index] = item % intervals[index][1]         

        self.position = Point(self.function, position_list).create_reference()

        if(self.position.get_value() < self.pBest.get_value()):
            self.pBest = self.position