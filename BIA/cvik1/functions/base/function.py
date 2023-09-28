import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Function():
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def calculate(self, params):
        pass

    def visualize(self, x1From, x1To, x2From, x2To, points, best_point):
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

        surf = ax.plot_surface(x1, x2, f1_2, cmap="jet")

        ax.set_xlabel("x1")
        ax.set_ylabel("x2")
        ax.set_zlabel("f(x1, x2)")

        plt.title(self.__class__.__name__ + " function")
        plt.show()