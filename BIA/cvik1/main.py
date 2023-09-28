import numpy as np

from functions.sphere import Sphere
from functions.ackley import Ackley
from functions.rastrigin import Rastrigin
from functions.rosenbrock import Rosenbrock
from functions.griewank import Griewank
from functions.schwefel import Schwefel
from functions.levy import Levy
from functions.michalewicz import Michalewicz
from functions.zakharov import Zakharov

from blindSearch import BlindSearch

if __name__ == "__main__":
    #functions a its axis ranges (used part of its domains of functions)
    sphere = Sphere()
    sphereRanges = [-10, 10, -6, 6]

    ackley = Ackley(a = 20, b = 0.2, c = 2 * np.pi)
    ackleyRanges = [-40, 40, -40, 40]

    rastrigin = Rastrigin()
    rastriginRanges = [-5, 5, -5, 5]

    rosenbrock = Rosenbrock()
    rosenbrockRanges = [-10, 10, -6, 6]

    k = 2
    griewank = Griewank()
    griewankRanges = [k * -5, k * 5, k * -5, k * 5]

    schwefel = Schwefel()
    schwefelRanges = [-500, 500, -500, 500]

    levy = Levy()
    levyRanges = [-10, 10, -10, 10]

    michalewicz = Michalewicz(m = 10)
    michalewiczRanges = [0, 4, 0, 4]

    zakharov = Zakharov()
    zakharovRanges = [-10, 10, -10, 10]
    
    #blindSearch
    blindSearch = BlindSearch(ackley)
    print(blindSearch.search(ackleyRanges, 30))