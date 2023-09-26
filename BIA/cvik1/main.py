import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Function():
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def calculate(self, params):
        pass

    def visualize(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1, projection='3d')

        x1axis = np.linspace(-10, 10, 500)
        x2axis = np.linspace(-10, 10, 500)
        x1, x2 = np.meshgrid(x1axis, x2axis)
        #f1_2 = func([x1, x2]) #rastrigin
        #f1_2 = func([x1, x2]) #rosenbrock
        #f1_2 = func([x1, x2]) #griewank
        #f1_2 = func([x1, x2]) #schwefel
        #f1_2 = func([x1, x2]) #levy
        #f1_2 = func(10, [x1, x2]) #michalewicz
        f1_2 = self.calculate([x1, x2]) #zakharov

        surf = ax.plot_surface(x1, x2, f1_2, cmap="jet")

        ax.set_xlabel("x1")
        ax.set_ylabel("x2")
        ax.set_zlabel("f(x1, x2)")

        plt.show()

class Sphere(Function):
    def calculate(self, params):
        ret = 0
        for xi in params:
            ret += xi**2

        return ret

class Ackley(Function):
    def calculate(self, params):
        d = len(params)

        #first
        sumx = 0
        for xi in params:
            sumx += xi**2

        sqrt = np.sqrt((1 / d) * sumx)
        exp_first = np.exp(-self.kwargs["b"] * sqrt)
        first = -self.kwargs["a"] * exp_first

        #second
        sumcos = 0
        for xi in params:
            sumcos += np.cos(self.kwargs["c"] * xi)

        second = np.exp((1 / d) * sumcos)

        #summary
        ret = first - second + self.kwargs["a"] + np.exp(1)

        return ret

class Rastrigin(Function):
    def calculate(self, params):
        d = len(params)

        #suma
        suma = 0
        for xi in params:
            suma += (xi**2 - 10 * np.cos(2 * np.pi * xi))

        #summary
        ret = 10 * d + suma

        return ret

class Rosenbrock(Function):
    def calculate(self, params):
        d = len(params)

        ret = 0
        for i in range(0, d - 1):
            xi = params[i]
            #first
            inner = params[i + 1 ] - xi**2
            first = 100 * inner**2

            #second
            second = (xi - 1)**2

            #summary
            ret += first + second

        return ret

class Griewank(Function):
    def calculate(self, params):
        #first
        suma = 0
        for xi in params:
            suma += xi**2 - 4000

        #second
        product = 0
        for i, xi in enumerate(params):
            product *= np.cos(xi / np.sqrt(i + 1)) + 1

        #summary
        ret = suma - product

        return ret

class Schwefel(Function):
    def calculate(self, params):
        d = len(params)

        #suma
        suma = 0
        for xi in params:
            suma += xi * np.sin(np.sqrt(np.abs(xi)))

        #summary
        ret = 418.9829 * d - suma

        return ret

class Levy(Function):
    def calculate(self, params):
        d = len(params)
        w = lambda i: 1 + ((params[i] - 1) / 4)

        #first
        first = np.sin(np.pi * w(0))**2

        #suma
        suma = 0
        for i in range(0, d - 1):
            xi = params[i]
            suma += (w(i) - 1)**2 * (1 + 10 * np.sin(np.pi * w(i) + 1)**2)

        #second
        second = (w(d - 1))**2 * (1 + np.sin(2 * np.pi * w(d - 1)**2))

        #summary
        ret = first + suma + second

        return ret

    def michalewicz(self, m, params):
        #suma
        suma = 0
        for i, xi in enumerate(params):
                suma += np.sin(xi) * np.sin((i * xi**2) / np.pi)**(2 * m)

        #summary
        ret = -suma

        return ret

    def zakharov(self, params):
        #first
        first = 0
        for xi in params:
            first += xi**2
        
        #second
        second = 0
        for i, xi in enumerate(params):
            second += 0.5 * i * xi

        #summary
        ret = first + second**2 + second**4

        return ret

    


if __name__ == "__main__":
    #sphere = Sphere()
    #sphere.visualize()

    #ackley = Ackley(a = 20, b = 0.2, c = 2 * np.pi)
    #ackley.visualize()

    #rastrigin = Rastrigin()
    #rastrigin.visualize()

    #rosenbrock = Rosenbrock()
    #rosenbrock.visualize()

    #griewank = Griewank() #????????
    #griewank.visualize()

    #schwefel = Schwefel()
    #schwefel.visualize()

    #levy = Levy()
    #levy.visualize()

    # přidat možnost nastavit velikosti os X a Y pro jednotlivé funkce (pomocí parametrů metody visualize)
    # rozdělit třídy do jednotlivých souborů
