from functions.base.function import Function

from cvik9.firefly import Firefly

Intervals = list[tuple[float, float]]

class Swarm:

    def __init__(self,
        function: Function,
        intervals: Intervals
    ):

        self.function: Function = function
        self.intervals: Intervals = intervals

    def generate_initial_population(self,
        individual_count: int                                
    ) -> list[Firefly]:

        initial_population: list[Firefly] = list()
        for _ in range(individual_count):
            individual: Firefly = Firefly(self.intervals)
            initial_population.append(individual)

        return initial_population

    def search(self,
        max_generation: int,
        individual_count: int,
        alpha: float
    ) -> float:
        
        population: list[Firefly] = self.generate_initial_population(individual_count = individual_count)

        for _ in range(max_generation):
            for current_individual in population:
                current_individual_value: float = current_individual.evaluate(self.function)
                for other_individual in population:
                    #not to move to self
                    if current_individual == other_individual:
                        continue
                    #calculate light intensity
                    other_individual_value: float = other_individual.evaluate(self.function)
                    if other_individual_value > current_individual_value:
                        other_individual.move_to(current_individual, alpha)

        best_firefly: Firefly = population[0]
        for index, firefly in enumerate(population):
            if firefly.evaluate(self.function) < best_firefly.evaluate(self.function):
                best_firefly = firefly
        population.remove(best_firefly)

        #print(best_firefly.solution, best_firefly.evaluate(self.function))

        #self.function.visualize(intervals = self.intervals,
        #                        best_point = best_firefly.get_reference_point(self.function),
        #                        points = [individual.get_reference_point(self.function) for individual in population])

        return best_firefly.get_reference_point(self.function).get_value()