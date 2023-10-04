from typing import List, Tuple

import numpy as np

from src.functions.point.reference_point import Reference_point

from src.functions.sphere import Sphere
from src.functions.ackley import Ackley
from src.functions.rastrigin import Rastrigin
from src.functions.rosenbrock import Rosenbrock
from src.functions.griewank import Griewank
from src.functions.schwefel import Schwefel
from src.functions.levy import Levy
from src.functions.michalewicz import Michalewicz
from src.functions.zakharov import Zakharov

from hill_climbing.hill_climbing import Hill_climbing

if __name__ == "__main__":
    #functions a its axis ranges (used part of its domains of functions)
    sphere: Sphere = Sphere()
    sphereIntervals: List[Tuple[int, int]] = [(-10, 10), (-6, 6)]

    ackley: Ackley = Ackley(a = 20, b = 0.2, c = 2 * np.pi)
    ackleyIntervals: List[Tuple[int, int]] = [(-40, 40), (-40, 40)]

    rastrigin: Rastrigin = Rastrigin()
    rastriginIntervals: List[Tuple[int, int]] = [(-5, 5), (-5, 5)]

    rosenbrock: Rosenbrock = Rosenbrock()
    rosenbrockIntervals: List[Tuple[int, int]] = [(-10, 10), (-6, 6)]

    k = 2
    griewank: Griewank = Griewank()
    griewankIntervals: List[Tuple[int, int]] = [(k * -5, k * 5), (k * -5, k * 5)]

    schwefel: Schwefel = Schwefel()
    schwefelIntervals: List[Tuple[int, int]] = [(-500, 500), (-500, 500)]

    levy: Levy = Levy()
    levyIntervals: List[Tuple[int, int]] = [(-10, 10), (-10, 10)]

    michalewicz: Michalewicz = Michalewicz(m = 10)
    michalewiczIntervals: List[Tuple[int, int]] = [(0, 4), (0, 4)]

    zakharov: Zakharov = Zakharov()
    zakharovIntervals: List[Tuple[int, int]] = [(-10, 10), (-10, 10)]

    #hill_climbing
    hill_climbing: Hill_climbing = Hill_climbing(zakharov)
    possible_global_minimum: Reference_point = hill_climbing.search(zakharovIntervals, 
                                                                    dim_avg_and_std_dev = (0, 2),
                                                                    count_of_neighbours = 5,
                                                                    count_of_itereations = 10)
    print(possible_global_minimum.get_params(), possible_global_minimum.get_value())