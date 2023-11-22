from typing import List

import unittest

from city import City
from solution import Solution
from travellingSalesmanGeneticAlgorithm import TravellingSalesmanGeneticAlgorithm

import math

class TSPGeneticAlogrithUnitTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        TSPGeneticAlogrithUnitTest.obj = TravellingSalesmanGeneticAlgorithm(5)
        city_A: City = City(0, 7, 5)
        city_B: City = City(1, 10, 0)
        city_C: City = City(2, 7, 6)
        city_D: City = City(3, 20, 4)
        city_E: City = City(4, 15, 7)
        TSPGeneticAlogrithUnitTest.obj.cities = [city_A, city_B, city_C, city_D, city_E]
        TSPGeneticAlogrithUnitTest.initial_population: List[Solution] = TSPGeneticAlogrithUnitTest.obj.create_initial_populate(5)

    def test_construct_distance_matrix(self) -> None:
        #print("-------------construct_distance_matrix-------------")
        expected: List[List[float]] = [[0.0, math.sqrt(34), 1.0],
                                       [math.sqrt(34), 0.0,  math.sqrt(45)],
                                       [1.0, math.sqrt(45), 0.0]]
        real: List[List[float]] = TSPGeneticAlogrithUnitTest.obj.construct_distance_matrix()
        #self.assertEqual(expected, real)

    def test_generate_random_solution(self) -> None:
        #print("-------------generate_random_solution-------------")
        random_initial_solution: Solution = TSPGeneticAlogrithUnitTest.obj.generate_random_solution()
        for city in random_initial_solution.cities:
            #print(city.index_id, city.x, city.y)
            pass

    def test_create_initial_population(self) -> None:
        #print("-------------create_initial_population-------------")
        TSPGeneticAlogrithUnitTest.initial_population: List[Solution] = TSPGeneticAlogrithUnitTest.obj.create_initial_populate(5)
        for i, solution in enumerate(TSPGeneticAlogrithUnitTest.initial_population):
            #print("Solution: ", i)
            for city in solution.cities:
                #print(city.index_id, city.x, city.y)
                pass

    def test_find_partner(self) -> None:
        #print("-------------find_partner-------------")
        first_parent: Solution = TSPGeneticAlogrithUnitTest.initial_population[1]
        for city in first_parent.cities:
            #print(city.index_id, city.x, city.y)
            pass

        #print("---------------")
        partner: Solution = TSPGeneticAlogrithUnitTest.obj.find_partner(1, TSPGeneticAlogrithUnitTest.initial_population)
        for city in partner.cities:
            #print(city.index_id, city.x, city.y)
            pass

    def test_copulate(self):
        print("-------------copulate-------------")
        parent_A: Solution = TSPGeneticAlogrithUnitTest.initial_population[1]
        parent_B: Solution = TSPGeneticAlogrithUnitTest.obj.find_partner(1, TSPGeneticAlogrithUnitTest.initial_population)

        child: Solution = TSPGeneticAlogrithUnitTest.obj.copulate(parent_A, parent_B)

        for city in parent_A.cities:
            print(city.index_id, city.x, city.y)
            pass

        print()
        for city in parent_B.cities:
            print(city.index_id, city.x, city.y)
            pass

        print()
        for city in child.cities:
            print(city.index_id, city.x, city.y)
            pass

    def test_find_shortest_path(self):
        print("-------------find_shortest_path-------------")
        gens_30: float = TSPGeneticAlogrithUnitTest.obj.find_shortest_path(30, 5)
        print(gens_30)
        gens_50: float = TSPGeneticAlogrithUnitTest.obj.find_shortest_path(50, 5)
        print(gens_50)
        gens_90: float = TSPGeneticAlogrithUnitTest.obj.find_shortest_path(90, 5)
        print(gens_90)
        gens_100: float = TSPGeneticAlogrithUnitTest.obj.find_shortest_path(100, 5)
        print(gens_100)
        gens_150: float = TSPGeneticAlogrithUnitTest.obj.find_shortest_path(150, 5)
        print(gens_150)
        gens_200: float = TSPGeneticAlogrithUnitTest.obj.find_shortest_path(200, 5)
        print(gens_200)

if __name__ == "__main__":
    unittest.main()