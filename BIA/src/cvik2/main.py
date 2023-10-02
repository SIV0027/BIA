from typing import List, Tuple

import numpy as np

from src.functions.ackley import Ackley
from src.functions.rastrigin import Rastrigin
#from src.functions.rosenbrock import Rosenbrock
#from src.functions.griewank import Griewank
#from src.functions.schwefel import Schwefel
#from src.functions.levy import Levy
#from src.functions.michalewicz import Michalewicz
#from src.functions.zakharov import Zakharov

from hill_climbing.hill_climbing import Hill_climbing

if __name__ == "__main__":
    #ackley: Ackley = Ackley(a = 20, b = 0.2, c = 2 * np.pi)
    #ackleyRanges: List[Tuple[float, float]] = [(-40, 40), (-40, 40)]
    #ackley.visualize(ackleyRanges, [0, 0, 0])

    #rastrigin: Rastrigin = Rastrigin()
    #rastriginRanges: List[Tuple[float, float]] = [(-5, 5), (-5, 5)]
    #rastrigin.visualize(rastriginRanges, [0, 0, 0])

    

    #hill_climbing: Hill_climbing = Hill_climbing(ackley)
    #hill_climbing.search(ackleyRanges)