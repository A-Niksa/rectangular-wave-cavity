from solving_routine.constants import *

class InitialConditionsManager:
    def set_initial_conditions(self, physical_system):
        first_grid = physical_system.get_grid_by_index(0)
        second_grid = physical_system.get_grid_by_index(1)

        self.set_value_grid_initial_conditions(first_grid.get_value_grid())
        self.set_value_grid_initial_conditions(second_grid.get_value_grid())

    def set_value_grid_initial_conditions(self, value_grid):
        value_grid[1:cols-1, 1] = 1
