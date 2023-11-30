import numpy as np

from cvik5.differential_evolution import Differential_evolution as DE
from cvik6.swarm import Swarm as PSO
from cvik7.soma import Soma as SOMA
from cvik9.swarm import Swarm as FA
from cvik10.sclass import SClass as TLBO

from functions.functions import Functions

if __name__ == "__main__":

    funcs = [
        ("ackley", Functions.ackley,{ "a": 20, "b": 0.2, "c": 2 * np.pi }),
        ("griewank", Functions.griewank, { }),
        ("levy", Functions.levy, { }),
        ("michalewicz", Functions.michalewicz, { "m": 10 }),
        ("rastrigin", Functions.rastrigin, { }),
        ("rosenbrock", Functions.rosenbrock, { }),
        ("schwefel", Functions.schwefel, { }),
        #("sphere", Functions.sphere, { }),
        ("zakharov", Functions.zakharov, { })
    ]

    methods = [
        (DE, { "number_of_population": 30, "number_of_generation": 20, "constant_F": 0.8, "constant_CR": 0.5 }),
        (PSO, { "migrations_count": 30, "particles_count": 30, "v_max": 0.2 }),
        (SOMA, { "pop_size": 30, "prt": 0.4, "path_length": 3.0, "step": 0.11, "m_max": 100 }),
        (FA, { "max_generation": 50, "individual_count": 30, "alpha": 0.5 }),
        (TLBO, { "max_iter": 100, "students_count": 30 })
    ]

    for func_name, func, func_params in funcs:
        print(func_name)
        function, intervals = func(**func_params)
        row_list = list()
        for _ in range(30):
            row = list()
            for method, method_params in methods:
                m = method(function, intervals)
                minimum: float = m.search(**method_params)
                row.append(minimum)
            row_list.append(row)
        
        f = open(f"{func_name}.csv", "w")
        for row in row_list:
            for n in row:
                f.write(str(n))
                f.write(";")
            f.write("\n")
        f.close()