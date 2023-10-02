from typing import List, Tuple

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Function():
    def __init__(self, 
        allowed_keys: List[str] = [],
        **kwargs):

        len_args_keys = len(kwargs.keys())
        len_allowed_keys = len(allowed_keys)
        if(len_args_keys < len_allowed_keys):
            raise ValueError(f"Not all variables have been entered to constructor of class {self.__class__.__name__}.")
        elif(len_args_keys > len_allowed_keys):
            raise ValueError(f"Too much variables have been entered to constructor of class {self.__class__.__name__}.")
        for key in kwargs.keys():
            if key not in allowed_keys:
                raise ValueError(f"Variable {key} is not allowed in constructor of class {self.__class__.__name__}.")

    #"abstract" method for overriding by concrete function
    #template for calcuation of the value by domain of function 
    def calculate(self, 
        params: List[float]) -> float:
        pass

    #visualizes concrete function
    def visualize(self, 
        intervals: List[Tuple[float, float]],
        best_point: List[float],
        points: List[List[float]] = []) -> None:

        xf, xs = intervals
        x1From, x1To = xf
        x2From, x2To = xs

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')

        ax.scatter([x[0] for x in points],
                   [x[1] for x in points],
                   [x[2] for x in points],
                   c = "purple", s = 50)
        ax.scatter(best_point[0], best_point[1], best_point[2], c = "red", s = 70)

        x1axis = np.linspace(x1From, x1To, 500)
        x2axis = np.linspace(x2From, x2To, 500)
        x1, x2 = np.meshgrid(x1axis, x2axis)
        f1_2 = self.calculate([x1, x2])

        surf = ax.plot_surface(x1, x2, f1_2, cmap="jet", alpha = 0.7)

        ax.set_xlabel("x1")
        ax.set_ylabel("x2")
        ax.set_zlabel("f(x1, x2)")

        plt.title(self.__class__.__name__ + " function")
        plt.show()