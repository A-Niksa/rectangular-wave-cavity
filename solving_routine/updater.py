from solving_routine.constants import *


class Updater:
    current_value_grid = []
    first_prev_value_grid = []
    second_prev_value_grid = []

    def update(self, grid, first_prev_grid, second_prev_grid):
        self.init_value_grids(grid, first_prev_grid, second_prev_grid)

        self.current_value_grid[1:rows-1, 1:cols-1] = (delta_t * c / delta_h) ** 2 * \
            (self.first_prev_value_grid[0:rows-2, 1:cols-1] + self.first_prev_value_grid[2:rows, 1:cols-1] +
             self.first_prev_value_grid[1:rows-1, 0:cols-2] + self.first_prev_value_grid[1:rows-1, 2:cols] -
             4 * self.first_prev_value_grid[1:rows-1, 1:cols-1]) + 2 * self.first_prev_value_grid[1:rows-1, 1:cols-1] - \
            self.second_prev_value_grid[1:rows-1, 1:cols-1]

        return self.current_value_grid

    def init_value_grids(self, grid, first_prev_grid, second_prev_grid):
        self.current_value_grid = grid.get_value_grid()
        self.first_prev_value_grid = first_prev_grid.get_value_grid()
        self.second_prev_value_grid = second_prev_grid.get_value_grid()