from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from solving_routine.constants import delta_t


class Animator:
    fig, ax = plt.subplots(1, 1)

    def __int__(self):
        self.fig.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    def render_animation(self, solution):
        def animate(i):
            grid = solution.get_grid_by_index(i)
            time = (i + 1) * delta_t

            self.ax.clear()
            self.ax.contourf(grid.get_x_meshgrid(), grid.get_y_meshgrid(), grid.get_value_grid()**2)
            self.ax.set_title = "Time: " + str(time) + " s"

        return FuncAnimation(self.fig, animate, frames=solution.get_solution_length(), repeat=True)
