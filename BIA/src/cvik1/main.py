import numpy as np

from src.functions.sphere import Sphere
from src.functions.ackley import Ackley
from src.functions.rastrigin import Rastrigin
from src.functions.rosenbrock import Rosenbrock
from src.functions.griewank import Griewank
from src.functions.schwefel import Schwefel
from src.functions.levy import Levy
from src.functions.michalewicz import Michalewicz
from src.functions.zakharov import Zakharov

from blind_search.blind_search import Blind_search

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
    
    #Blind Search
    blind_search = Blind_search(ackley)
    print(blind_search.search(ackleyRanges, 30))