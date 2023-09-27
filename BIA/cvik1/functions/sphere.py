from functions.base.function import Function

class Sphere(Function):
    def calculate(self, params):
        ret = 0
        for xi in params:
            ret += xi**2

        return ret