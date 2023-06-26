from geometry.grid import Grid


class PhysicalSystem:
    rows = 1
    cols = 1
    grid_profile = []

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        grid = Grid(rows, cols)
        self.grid_profile.append(grid)
        self.grid_profile.append(grid)  # this should be done twice

    def get_grid_by_index(self, index):
        return self.grid_profile[index]

    def append_value_grid(self, value_grid):
        new_grid = Grid(self.rows, self.cols)
        new_grid.set_value_grid(value_grid)
        self.grid_profile.append(new_grid)

    def get_solution_length(self):
        return len(self.grid_profile)
