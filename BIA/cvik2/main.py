import numpy as np

from functions.ackley import Ackley

if __name__ == "__main__":
    ackley = Ackley(a = 20, b = 0.2, c = 2 * np.pi)
    ackleyRanges = [-40, 40, -40, 40]

    x1From, x1To, x2From, x2To = ackleyRanges
    ackley.visualize(x1From, x1To, x2From, x2To, [], [0, 0, 0])