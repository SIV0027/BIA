from typing import List

import random

from city import City

class Solution:
    def __init__(self, cities: List[City], distance_matrix: List[List[float]]):
        #list of cities
        self.cities: List[City] = cities
        #start city as end (cycle)
        self.cities.append(self.cities[0])
        #distance of travel (solution)
        self.distance: float = self.calculate_measure_distance(distance_matrix)

    #measure distance of travel (current solution)
    def calculate_measure_distance(self, distance_matrix: List[List[float]]) -> float:
        measure_distance: float = 0.0

        count_of_cities_in_solution = len(self.cities)
        for i in range(count_of_cities_in_solution - 1):
            #cities
            current_city: City = self.cities[i]
            next_city: City = self.cities[i + 1]
            #indexes of cities
            current_city_index: int = current_city.index_id
            next_city_index: int = next_city.index_id
            #distance between "current_city" and "next_city"
            measure_distance += distance_matrix[current_city_index][next_city_index]

        return measure_distance

    def mutate(self) -> None:
        l = len(self.cities)
        first: int = random.randint(1, l - 1)
        second: int = -1
        while True:
            second = random.randint(1, l - 1)
            if second != first:
                break

        tmp: City = self.cities[first]
        self.cities[first] = self.cities[second]
        self.cities[second] = tmp