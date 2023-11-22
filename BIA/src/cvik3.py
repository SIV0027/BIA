from functions.functions import Functions
from search_methods.simulatedAnnealing.simulatedAnnealing import SimulatedAnnealing

if __name__ == "__main__":

    sphere, sphereIntervals = Functions.sphere()
    michalewicz, michalewiczIntervals = Functions.michalewicz(m = 10)
    levy, levyIntervals = Functions.levy()

    sa: SimulatedAnnealing = SimulatedAnnealing(sphere)
    sa.search(sphereIntervals, t_0 = 100, t_min = 0.5, alpha = 0.95)