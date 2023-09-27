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
    #sphere = Sphere()
    #sphere.visualize(-10, 10, -6, 6)

    #ackley = Ackley(a = 20, b = 0.2, c = 2 * np.pi)
    #ackley.visualize(-40, 40, -40, 40)

    #rastrigin = Rastrigin()
    #rastrigin.visualize(-5, 5, -5, 5)

    #rosenbrock = Rosenbrock()
    #rosenbrock.visualize(-10, 10, -6, 6)

    #k = 2
    #griewank = Griewank()
    #griewank.visualize(k * -5, k * 5, k * -5, k * 5)

    #schwefel = Schwefel()
    #schwefel.visualize(-500, 500, -500, 500)

    #levy = Levy()
    #levy.visualize(-10, 10, -10, 10)

    #michalewicz = Michalewicz(m = 10) # poss ?
    #michalewicz.visualize(0, 4, 0, 4)

    zakharov = Zakharov()
    zakharov.visualize(-10, 10, -10, 10)
