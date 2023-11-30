from cvik6.swarm import Swarm

from functions.functions import Functions

if __name__ == "__main__":
    
    function, intervals = Functions.michalewicz(m = 10)

    swarm: Swarm = Swarm(function, intervals)
    swarm.search(migrations_count = 30,
                 particles_count = 30,
                 v_max = 0.2)