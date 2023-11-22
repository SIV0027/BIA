import pandas as pd

from functions.base.function import Function
from functions.point.reference_point import Reference_point

from cvik7.spicemen import Spicemen

Intervals = list[tuple[float, float]]

class Soma:
    
    def __init__(self,
        function: Function,
        intervvals: Intervals
    ):
        
        self.function: Function = function
        self.intervals: Intervals = intervvals

        self.leader: Spicemen

    def search_minimum(self,
        pop_size: int,
        prt: float,
        path_length: float,
        step: float,
        m_max: 100
    ) -> None:
        
        population: list[Spicemen] = list()
        self.leader = Spicemen(function = self.function,
                               intervals = self.intervals,
                               step = step,
                               path_length = path_length,
                               prt = prt)
        population.append(self.leader)

        for _ in range(pop_size - 1):
            spicemen: Spicemen = Spicemen(function = self.function,
                                          intervals = self.intervals,
                                          step = step,
                                          path_length = path_length,
                                          prt = prt)
            population.append(spicemen)
            if spicemen.get_value() < self.leader.get_value():
                self.leader = spicemen
        
        """for spicemen in population:
            print(spicemen.get_value())

        print()
        print(self.leader.get_value())"""

        previous_leaders: list[Reference_point] = list()
        for _ in range(m_max):
            leader_position: pd.Series = pd.Series(self.leader.get_params())

            potentional_leader: Spicemen
            for spicemen in population:
                if spicemen != self.leader:
                    spicemen.migrate(leader_position)
                    potentional_leader = spicemen

            for spicemen in population:
                if spicemen != self.leader:
                    if spicemen.get_value() < potentional_leader.get_value():
                        potentional_leader = spicemen

            if potentional_leader.get_value() < self.leader.get_value():
                previous_leaders.append(self.leader)
                self.leader = potentional_leader

        self.function.visualize(intervals = self.intervals,
                                best_point = self.leader.get_point(),
                                points = previous_leaders)