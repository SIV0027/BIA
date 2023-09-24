import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Solution:
    def __init__(self, name):
        self.name = name

    def sphere(self, params):
        ret = 0

        for i in params:
            ret += i**2

        return ret

    def visualize(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')

        x1axis = np.linspace(-5, 5, 100)
        x2axis = np.linspace(-5, 5, 100)
        x1, x2 = np.meshgrid(x1axis, x2axis)
        f1_2 = self.sphere([x1, x2])

        surf = ax.plot_surface(x1, x2, f1_2, cmap="jet")

        ax.set_xlabel("x1")
        ax.set_ylabel("x2")
        ax.set_zlabel("f(x1, x2)")

        plt.show()


if __name__ == "__main__":
    sl = Solution("Sphere")
    sl.visualize()