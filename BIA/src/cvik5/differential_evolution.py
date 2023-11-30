from typing import List, Tuple

from functions.point.point import Point
from functions.point.reference_point import Reference_point
from functions.base.function import Function

import copy
import random

Intervals = List[Tuple[float, float]]

#class which implements differential_evolution
class Differential_evolution:
    def __init__(self,
    function: Function, 
    intervals: Intervals):
    
        self.function: Function = function
        self.intervals: Intervals = intervals

    #generate initial radnom population (by "number_of_population")
    def generate_inital_population(self,
    number_of_population: int) -> List[Reference_point]:

        initial_population: List[Reference_point] = []
        #dodělat kontrolu duplikátů
        for _ in range(number_of_population):
            x: float = random.uniform(self.intervals[0][0], self.intervals[0][1])
            y: float = random.uniform(self.intervals[1][0], self.intervals[1][1])
            individual: Point = Point(self.function, [x, y])
            initial_population.append(individual.create_reference())

        return initial_population

    #return three random chosen different parents (vectors - points),
    #which is not "parent_A"
    def choose_random_parents(self,
    parent_A_index: int,
    population: List[Reference_point]) -> List[Reference_point]:

        end_random_index: int = len(population) - 1

        #list of indexes of chosen parents
        random_chosen_parents_indexes: List[int] = []
        #choose three random parents indexes (numbers is more useful)
        for _ in range(3):
            random_parent_index: int = random.randint(0, end_random_index)
            while random_parent_index == parent_A_index or random_parent_index in random_chosen_parents_indexes:
                random_parent_index = random.randint(0, end_random_index)
            random_chosen_parents_indexes.append(random_parent_index)
        
        #list of returned chosen parents
        random_chosen_parents: List[Reference_point] = [population[random_chosen_parents_indexes[0]],
                                                        population[random_chosen_parents_indexes[1]],
                                                        population[random_chosen_parents_indexes[2]]]

        return random_chosen_parents

    def search(self,
    number_of_population: int,
    number_of_generation: int,
    constant_F: float,
    constant_CR: float
    ) -> float:    

        #best vector (individual or solution)
        best_vector: Reference_point
        #array of previous best vectors (individuals or solutions) - because of visualization
        #(progress of algorithm)
        previous_best_vectors: List[Reference_point] = []

        #1. generate random population
        population: List[Reference_point] = self.generate_inital_population(number_of_population)
        #initialize of "best_vector" (because of "None" value)
        best_vector = population[0]
        
        #2. main loop (by "number_of_generation")
        generation_id: int = 1
        for _ in range(number_of_generation):
            new_population: List[Reference_point] = copy.deepcopy(population)
            #for each vector (point) - "target_vector", random choose three different vectors (parents)
            #and make new individual from them and mutate the new individual and choose current best
            for i, target_vector in enumerate(population):
                #random choose three different vectors (parents) then crossover and mutation is done
                first_random_vector, second_random_vector, third_random_vector = self.choose_random_parents(i, population)
                different_vector: Reference_point = first_random_vector - second_random_vector
                weight_different_vector = different_vector * constant_F
                noise_vector: Reference_point = third_random_vector + weight_different_vector
                #check and "return" values to the defined intervals ("self.intervals") of function (by "%" operator)
                noise_vector_params = noise_vector.get_params()
                for j, param in enumerate(noise_vector_params):
                    noise_vector.params[j] = param % self.intervals[j][1]
                #creating a test vector
                target_vector_params: List[float] = target_vector.get_params()
                noise_vector_params: List[float] = noise_vector.get_params()

                test_vector_params: List[float] = []
                for j, target_vector_param in enumerate(target_vector_params):
                    noise_vector_param: float = noise_vector_params[j]
                    random_number: float = random.uniform(0, 1)
                    if random_number < constant_CR:
                        test_vector_params.append(noise_vector_param)
                    else:
                        test_vector_params.append(target_vector_param)
                test_vector: Reference_point = Point(self.function, test_vector_params).create_reference()
                #comparsion of value of "test_vector" and "target_vector" and choosing better vector (individual)
                #to inclusion to current population (is new individual (value of "test_vector") better than
                #current individual (value of "target_vector")
                test_vector_value: float = test_vector.get_value()
                target_vector_value: float = target_vector.get_value()
                if test_vector_value < target_vector_value:
                    new_population[i] = test_vector
                else:
                    new_population[i] = target_vector
            
            #comparing of best value of individual (vector) of current generation ("new_generation")
            #with current best indiviudal (vector) ("best_vector") and eventually "previous_best_vectors"
            #is updated
            best_vector_value: float = best_vector.get_value()
            for current_vector in new_population:
                current_vector_value: float = current_vector.get_value()
                if current_vector_value < best_vector_value:
                    #update of "previous_best_vectors"
                    previous_best_vectors.append(best_vector)
                    best_vector = current_vector
            #replacing old population by new population (which has at least same "quality")
            population = new_population
        
        #visualization of results
        #print(previous_best_vectors)
        #self.function.visualize(self.intervals, best_vector, previous_best_vectors)

        return best_vector.get_value()