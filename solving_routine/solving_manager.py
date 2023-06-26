from geometry.grid import Grid
from geometry.physical_system import PhysicalSystem
from solving_routine.initial_conditions_manager import InitialConditionsManager
from solving_routine.updater import Updater
from solving_routine.constants import *


class SolvingManager:
    physical_sys = None
    updater = None
    initial_conditions_manager = None
    n_steps = int(end_t / delta_t)

    def __init__(self):
        self.physical_sys = PhysicalSystem(rows, cols)
        self.updater = Updater()
        self.initial_conditions_manager = InitialConditionsManager()

    def solve(self):
        self.initial_conditions_manager.set_initial_conditions(self.physical_sys)

        for i in range(2, self.n_steps):
            grid = Grid(rows, cols)
            first_prev_grid = self.physical_sys.get_grid_by_index(i-1)
            second_prev_grid = self.physical_sys.get_grid_by_index(i-2)
            value_grid = self.updater.update(grid, first_prev_grid, second_prev_grid)
            self.physical_sys.append_value_grid(value_grid)

    def get_solution(self):
        return self.physical_sys
