import numpy as np

class BlindSearch:
    def __init__(self, func):
        self.func = func

    def generate_solution(self, x1From, x1To, x2From, x2To):
        ret = []

        ret.append(np.random.randint(x1From, x1To))
        ret.append(np.random.randint(x2From, x2To))

        return ret

    def search(self, ranges, count):
        x1From, x1To, x2From, x2To = ranges
        best_solution = self.generate_solution(x1From, x1To, x2From, x2To)
        best_value = self.func.calculate(best_solution)

        best_point = [best_solution[0], best_solution[1], best_value]
        points = []

        for i in range(0, count):
            random_solution = self.generate_solution(x1From, x1To, x2From, x2To)
            random_solution_value = self.func.calculate(random_solution)

            if random_solution_value < best_value:
                best_solution = random_solution
                best_value = random_solution_value
                points.append([best_solution[0], best_solution[1], best_value])
                best_point = [random_solution[0], random_solution[1], random_solution_value]
            else:            
                points.append([random_solution[0], random_solution[1], random_solution_value])

        
        self.func.visualize(x1From, x1To, x2From, x2To, points, best_point)

        return [best_solution, best_value]
