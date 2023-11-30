from cvik7.soma import Soma

from functions.functions import Functions

if __name__ == "__main__":

    function, intervals = Functions.michalewicz(m = 10)

    soma: Soma = Soma(function, intervals)
    soma.search(pop_size = 20,
                prt = 0.4,
                path_length = 3.0,
                step = 0.11,
                m_max = 100)