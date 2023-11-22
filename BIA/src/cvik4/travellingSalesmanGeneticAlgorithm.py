from typing import List

import random
import matplotlib.pyplot as plt

from city import City
from solution import Solution

class TravellingSalesmanGeneticAlgorithm:
    def __init__(self, count_of_cities: int):
        #count of citites
        self.count_of_cities: int = count_of_cities
        #list of cities init by generate_cities method
        self.cities: List[City] = self.generate_cities()
        #distance matrix of cities init by construct_distance_matrix method
        self.distance_matrix: List[List[float]] = self.construct_distance_matrix()

    #generate (create) cities
    def generate_cities(self) -> List[City]:
        cities: List[City] = []

        for index_id in range(self.count_of_cities):
            x_coord: float = random.uniform(0.0, 100.0)
            y_coord: float = random.uniform(0.0, 100.0)
            city: City = City(index_id, x_coord, y_coord)
            cities.append(city)

        return cities

    #construct distance matrix (by euclid distance)
    def construct_distance_matrix(self) -> List[List[float]]:
        distance_matrix: List[List[float]] = []
    
        for i in range(self.count_of_cities):
            current_city: City = self.cities[i]
            row: List[float] = []
            for j in range(self.count_of_cities):
                other_city: City = self.cities[j]
                #euclid distance
                distance = ((current_city.x - other_city.x)**2 + (current_city.y - other_city.y)**2)**0.5
                row.append(distance)
            distance_matrix.append(row)
    
        return distance_matrix

    #create initial population
    def create_initial_populate(self, count_of_population: int) -> List[Solution]:
        initial_population: List[Solution] = []
        for _ in range(count_of_population):
            random_solution: Solution = self.generate_random_solution()
            initial_population.append(random_solution)

        return initial_population

    #generate radnom solution
    def generate_random_solution(self) -> Solution:
        copy_of_cities: List[City] = self.cities.copy()
        #start city is fixed => remove from random permutation
        start_city: Solution = copy_of_cities.pop(0)
        random.shuffle(copy_of_cities)
        #start city must be returned to first (index 0) position of solution
        copy_of_cities.insert(0, start_city)
        random_solution: Solution = Solution(copy_of_cities, self.distance_matrix)

        return random_solution

    #visualizes current state of solution (current generation)
    def visualize(self, best_solution: Solution) -> None:        
        plt.scatter([city.x for city in best_solution.cities], [city.y for city in best_solution.cities], color="blue")
        plt.plot([city.x for city in best_solution.cities], [city.y for city in best_solution.cities], color="red", linestyle="--")

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.show()

    #finds second parent to child
    def find_partner(self, first_parent_index: int, population: List[Solution]) -> Solution:
        #index must be different from "first_parent_index"
        count_of_poupulation: int = len(population)
        second_parent_index: int = -1
        while True:
            second_parent_index = random.randint(0, count_of_poupulation - 1)
            if second_parent_index != first_parent_index:
                break

        partner: Solution = population[second_parent_index]

        return partner

    #creates new solution (child) by two already existing solutions (parents) => crossover
    def copulate(self, parent_A: Solution, parent_B: Solution) -> Solution:
        half_length: int = self.count_of_cities // 2
        first_half_DNA: List[City] = parent_A.cities[:half_length]
        second_half_DNA: List[City] = parent_B.cities[half_length:]
        second_half_DNA.pop()

        #collision check
        #offset of last chosen city in collision buffer (first half of parent_B cities)
        offset = 0
        for i, city in enumerate(second_half_DNA):
            if city in first_half_DNA:
                l = len(parent_B.cities)
                for j in range(offset, half_length):
                    possible_city = parent_B.cities[j]
                    if possible_city not in first_half_DNA and possible_city not in second_half_DNA:
                        second_half_DNA[i] = possible_city
                
                offset += i + 1

        dna: List[City] = first_half_DNA + second_half_DNA
        child: Solution = Solution(dna, self.distance_matrix)

        return child
    
    def choose_best_solution(self, population: List[Solution]) -> Solution:
        best_solution: Solution = population[0]
        l: int = len(population)
        for i in range(1, l):
            solution = population[i]
            if solution.distance < best_solution.distance:
                best_solution = solution

        return best_solution

    #genetic algorithm which finds the shortest path in travelling salesman problem
    def find_shortest_path(self, count_of_generations: int, count_of_population: int) -> float:
        #1. generate population
        population: List[Solution] = self.create_initial_populate(count_of_generations)

        #2. main loop (by "count_of_generations")
        for _ in range(count_of_generations):
            current_population: List[Solution] = population.copy()
            for i in range(1, count_of_population):
                parent_A: Solution = current_population[i]
                parent_B: Solution = self.find_partner(i, current_population)

                child: Solution = self.copulate(parent_A, parent_B)
                #mutation
                if random.random() < 0.5:
                    child.mutate()
                
                #is chldren better than parent?
                if child.distance < parent_A.distance:
                    current_population[i] = child

            population = current_population

        #choice of best Soluion from "population"
        best_solution: Solution = self.choose_best_solution(population)
        self.visualize(best_solution)

        return best_solution.distance