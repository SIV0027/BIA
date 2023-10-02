from typing import List, Tuple

import numpy as np

class Blind_search:
    def __init__(self, func):
        self.func = func

    def generate_solution(self,
        intervals: List[Tuple[int, int]]) -> List[int]:

        ret: List[int] = []

        for interval in intervals:
            start, end = interval
            ret.append(np.random.randint(start, end))

        return ret

    def search(self,
        intervals: List[Tuple[int, int]],
        count) -> Tuple[List[int], float]:

        best_solution: List[int] = self.generate_solution(intervals)
        best_value: float = self.func.calculate(best_solution)

        best_point: List[float] = [best_solution[0], best_solution[1], best_value]
        points: List[List[float]] = []

        for i in range(0, count):
            random_solution: List[int] = self.generate_solution(intervals)
            random_solution_value: float = self.func.calculate(random_solution)

            if random_solution_value < best_value:
                best_solution = random_solution
                best_value = random_solution_value
                points.append([best_solution[0], best_solution[1], best_value])
                best_point = [random_solution[0], random_solution[1], random_solution_value]
            else:            
                points.append([random_solution[0], random_solution[1], random_solution_value])

        
        self.func.visualize(intervals, best_point, points)

        ret: Tuple[List[int], float] = (best_solution, best_value)

        return ret
