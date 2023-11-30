import random

import numpy as np

from functions.base.function import Function

from cvik10.student import Student

Intervals = list[tuple[float, float]]

class SClass:

    def __init__(self,
        function: Function,
        intervals: Intervals
    ):

        self.function: Function = function
        self.intervals: Intervals = intervals

    def generate_initial_population(self,
        individual_count: int                                
    ) -> list[Student]:

        initial_population: list[Student] = list()
        for _ in range(individual_count):
            individual: Student = Student(self.intervals)
            initial_population.append(individual)

        return initial_population
    
    def choose_worst(self,
        population: list[Student]
    ) -> Student:
        
        worst: Student = population[0]
        for student in population:
            if student.evaluate(self.function) > worst.evaluate(self.function):
                worst = student

        return worst
    
    def choose_partner(self,
        population: list[Student],
        current: Student
    ) -> Student:

        potentional_partners: list[Student] = list()
        for student in population:
            if student != current:
                potentional_partners.append(student)

        chosen_index: int = random.randint(0, len(potentional_partners) - 1)
        partner: Student = potentional_partners[chosen_index]

        return partner
    
    def calculate_mean(self,
        population: list[Student]                   
    ) -> float:

        mean: float = 0
        for student in population:
            mean += student.evaluate(self.function)

        mean /= len(population)

        return mean

    def search(self,
        students_count: int,
        max_iter: int
    ) -> float:
        
        population: list[Student] = self.generate_initial_population(students_count)
        for _ in range(max_iter):
            for student in population:
                #teaching phase
                x_teacher: Student = self.choose_worst(population = population) #choose worst
                x_mean: float = self.calculate_mean(population = population) #calculate mean
                tf = random.randint(1, 3) #generate random 1 or 2
                r: float = random.uniform(0, 1) #generate random number between 0 and 1
                x_new: np.ndarray = student.solution + r * (x_teacher.solution - tf * x_mean)
                x_new_student: Student = Student(self.intervals)
                x_new_student.solution = x_new
                if x_new_student.evaluate(self.function) < x_teacher.evaluate(self.function): #is better?
                    x_teacher.solution = x_new #then accept
                    x_teacher.check_bounds()

                #learning phase
                x_partner: Student = self.choose_partner(population = population,
                                                         current = student) #choose partner
                
                #plus or minus by evaluate
                if(student.evaluate(self.function) < x_partner.evaluate(self.function)):
                    x_new = student.solution + r * (student.solution - x_partner.solution)
                else:
                    x_new = student.solution - r * (student.solution - x_partner.solution)

                x_new_student = Student(self.intervals)
                x_new_student.solution = x_new
                if x_new_student.evaluate(self.function) < student.evaluate(self.function): #is better?
                    student.solution = x_new #then accept
                    student.check_bounds()

        #choose best solution
        best_solution: Student = population[0]
        for student in population:
            if student.evaluate(self.function) < best_solution.evaluate(self.function):
                best_solution = student
        population.remove(best_solution)

        print(best_solution.solution, best_solution.evaluate(self.function))

        self.function.visualize(intervals = self.intervals,
                                best_point = best_solution.get_reference_point(self.function),
                                points = [student.get_reference_point(self.function) for student in population])

        return best_solution.get_reference_point(self.function).get_value()