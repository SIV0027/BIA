from functions.functions import Functions

from cvik5.differential_evolution import Differential_evolution

if __name__ == "__main__":

    function, intervals = Functions.sphere()

    differential_evolution: Differential_evolution = Differential_evolution(function, intervals)
    differential_evolution.search(
        number_of_population = 10,
        number_of_generation = 20,
        constant_F = 0.8,
        constant_CR = 0.5
    )