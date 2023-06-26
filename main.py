# Arsha Niksa
# Student Number: 400108706
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

from plotting.animator import Animator
from solving_routine.solving_manager import SolvingManager

if __name__ == '__main__':
    manager = SolvingManager()
    manager.solve()

    animator = Animator()
    anim = animator.render_animation(manager.get_solution())

    anim.save("result.gif", dpi=300, writer=PillowWriter(fps=20))
