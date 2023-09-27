import numpy as np

from sphere import Sphere
from ackley import Ackley
from rastrigin import Rastrigin
from rosenbrock import Rosenbrock
from griewank import Griewank
from schwefel import Schwefel
from levy import Levy
from michalewicz import Michalewicz
from zakharov import Zakharov

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
