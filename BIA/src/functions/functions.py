from typing import Tuple

import numpy as np

from search_methods.base.intervals import Intervals

from functions.base.function import Function
from functions.sphere import Sphere
from functions.ackley import Ackley
from functions.rastrigin import Rastrigin
from functions.rosenbrock import Rosenbrock
from functions.griewank import Griewank
from functions.schwefel import Schwefel
from functions.levy import Levy
from functions.michalewicz import Michalewicz
from functions.zakharov import Zakharov

class Functions:

    @staticmethod
    def sphere() -> Tuple[Function, Intervals]:
        sphere: Sphere = Sphere()
        sphereIntervals: Intervals = [(-10, 10), (-6, 6)]

        return (sphere, sphereIntervals)
    
    @staticmethod
    def ackley(**kwargs) -> Tuple[Function, Intervals]:
        ackley: Ackley = Ackley(a = 20, b = 0.2, c = 2 * np.pi)
        ackleyIntervals: Intervals = [(-40, 40), (-40, 40)]

        return (ackley, ackleyIntervals)
    
    @staticmethod
    def rastrigin() -> Tuple[Function, Intervals]:
        rastrigin: Rastrigin = Rastrigin()
        rastriginIntervals: Intervals = [(-5, 5), (-5, 5)]
        
        return (rastrigin, rastriginIntervals)
    
    @staticmethod
    def rosenbrock() -> Tuple[Function, Intervals]:
        rosenbrock: Rosenbrock = Rosenbrock()
        rosenbrockIntervals: Intervals = [(-10, 10), (-6, 6)]

        return (rosenbrock, rosenbrockIntervals)
    
    @staticmethod
    def griewank(k: int = 2) -> Tuple[Function, Intervals]:
        griewank: Griewank = Griewank()
        griewankIntervals: Intervals = [(k * -5, k * 5), (k * -5, k * 5)]

        return (griewank, griewankIntervals)
    
    @staticmethod
    def schwefel() -> Tuple[Function, Intervals]:
        schwefel: Schwefel = Schwefel()
        schwefelIntervals: Intervals = [(-500, 500), (-500, 500)]
        
        return (schwefel, schwefelIntervals)
    
    @staticmethod
    def levy() -> Tuple[Function, Intervals]:
        levy: Levy = Levy()
        levyIntervals: Intervals = [(-10, 10), (-10, 10)]
        
        return (levy, levyIntervals)
    
    @staticmethod
    def michalewicz(**kwargs) -> Tuple[Function, Intervals]:
        michalewicz: Michalewicz = Michalewicz(**kwargs)
        michalewiczIntervals: Intervals = [(0, 4), (0, 4)]
        
        return (michalewicz, michalewiczIntervals)
    
    @staticmethod
    def zakharov() -> Tuple[Function, Intervals]:        
        zakharov: Zakharov = Zakharov()
        zakharovIntervals: Intervals = [(-10, 10), (-10, 10)]
        
        return (zakharov, zakharovIntervals)