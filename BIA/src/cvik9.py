from functions.functions import Functions
from cvik9.swarm import Swarm

if __name__ == "__main__":

    function, intervals = Functions.michalewicz(m = 10)

    swarm: Swarm = Swarm(function, intervals)
    swarm.search(max_generation = 50,
                 individual_count = 10,
                 alpha = 0.5)