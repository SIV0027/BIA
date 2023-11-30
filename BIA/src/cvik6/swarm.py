import random

from functions.base.function import Function
from functions.point.point import Point
from functions.point.reference_point import Reference_point

from cvik6.particle import Particle

Intervals = list[tuple[float, float]]

class Swarm:

    def __init__(self,
    function: Function,
    intervals: Intervals):

        self.function: Function = function
        self.intervals: Intervals = intervals

        self.gBest: Reference_point

    def set_gBest(self,
    gBest: Reference_point) -> None:
        
        self.gBest = gBest

    def generate_random_solution(self) -> list[float]:

        params: list[float] = list()
    
        params.append(random.uniform(self.intervals[0][0], self.intervals[0][1]))
        params.append(random.uniform(self.intervals[1][0], self.intervals[1][1]))

        return params

    def search(self,
    migrations_count: int,    
    particles_count: int,
    v_max: float,
    c1: int = 2,
    c2: int = 2
    ) -> float:
        
        #init gBest by random solution
        self.gBest = Point(self.function, self.generate_random_solution()).create_reference()
        #generate random population of particles
        population: list[Particle] = list()
        for _ in range(particles_count):
            random_individual_params: list[float] = self.generate_random_solution()
            random_individual_speed: list[float] = [random.uniform(0.01, abs(self.intervals[0][0]) + abs(self.intervals[0][1]) / 20),
                                                    random.uniform(0.01, abs(self.intervals[1][0]) + abs(self.intervals[1][1]) / 20)]
            random_individual: Particle = Particle(self.function, random_individual_params, random_individual_speed)
            #is position of individual better than current gBest?
            if(random_individual.position.get_value() < self.gBest.get_value()):
                self.gBest = random_individual.position
            population.append(random_individual)

        previous_best: list[Reference_point] = list() 
        #algorithm progress
        for _ in range(migrations_count):
            for particle in population:
                particle.calculate_speed(c1,c2, self.gBest, v_max)
                particle.move(self.intervals)
                if(particle.pBest.get_value() < self.gBest.get_value()):
                    previous_best.append(self.gBest)
                    self.gBest = particle.pBest

        #self.function.visualize(self.intervals, self.gBest, previous_best)

        return self.gBest.get_value()

        

        