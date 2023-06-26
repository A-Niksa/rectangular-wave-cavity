from matplotlib import pyplot as plt

class GridPlotter:
    def plot_grid(self, grid, time):
        fig, ax = plt.subplots(1, 1)
        cp = ax.contourf(grid.get_x_meshgrid(), grid.get_y_meshgrid(), grid.get_value_grid())
        ax.set_title = "Time: " + str(time)
        return fig