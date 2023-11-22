from functions.functions import Functions

from cvik5.differential_evolution import Differential_evolution

if __name__ == "__main__":

    function, intervals = Functions.sphere()

    differential_evolution: Differential_evolution = Differential_evolution(function, intervals)
    differential_evolution.search_minimum(10, 20, 0.8, 0.5)