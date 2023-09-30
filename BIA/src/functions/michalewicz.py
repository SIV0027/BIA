import numpy as np
from functions.base.function import Function

class Michalewicz(Function):
    def calculate(self, params):
        #suma
        suma = 0
        for i, xi in enumerate(params):
                suma += np.sin(xi) * np.sin(((i + 1) * xi**2) / np.pi)**(2 * self.kwargs["m"])

        #summary
        ret = -suma

        return ret