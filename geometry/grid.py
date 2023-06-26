import numpy as np


class Grid:
    rows = 1
    cols = 1
    x_meshgrid = []
    y_meshgrid = []
    value_grid = []

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.value_grid = np.zeros((rows, cols))
        self.init_meshgrid()

    def init_meshgrid(self):
        x = np.zeros(self.rows)
        y = np.zeros(self.cols)
        self.x_meshgrid, self.y_meshgrid = np.meshgrid(x, y)

    def get_x_meshgrid(self):
        return self.x_meshgrid

    def get_y_meshgrid(self):
        return self.y_meshgrid

    def get_value_grid(self):
        return self.value_grid

    def set_value_grid(self, value_grid):
        self.value_grid = value_grid
