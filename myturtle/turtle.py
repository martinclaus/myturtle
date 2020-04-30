""" Simple turtle class based on matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np


class Turtle(object):
    """Turtel cursor class

    The turtle can turn left or right and move forward. It will draw a line
    if drawing is switch on, which it is by default. This version of turtle is
    using matplotlib for drawing and may be used in Jupyter notebooks.

    Methods:
    --------
    left(turn=90): turn left by `turn` degrees
    right(turn=90): turn right by `turn` degrees
    forward(distance=1): move forward by `distance`
    set_draw(draw=True): set draw state to either True or False
    reset(): reset prosition and angle of the turtle to initial values
    """

    def __init__(self, color='k'):

        # x position
        self.x = 0

        # y  position
        self.y = 0

        # angle of turtle in rad
        self.angle = 0

        # coordinated of position
        self.position = [self.x, self.y]

        # state of pen
        self.draw = True
        self.color = color

        self.reset()


    def reset(self):
        self.set_x(0.)
        self.set_y(0.)
        self.angle = 0.
        self.draw = True

    def left(self, turn=90):
        """Turn left

        Parameter:
        ----------
        turn: numeric, default=90. Degrees to turn left
        """
        self.angle += np.pi * turn / 180.


    def right(self, turn=90):
        """Turn right

        Parameter:
        ----------
        turn: numeric, default=90. Degrees to turn right
        """
        self.left(-turn)



    def forward(self, distance=1):
        """Move forward

        Parameter:
        ---------
        distance: numeric, default=1. Distance to move forward
        """
        dx = np.cos(self.angle) * distance
        dy = np.sin(self.angle) * distance

        p1 = self.position.copy()
        p1[0] += dx
        p1[1] += dy
        self.move(p1)


    def move(self, p1, p0=None, draw=None):
        """Move from position p0 to p1

        Parameter:
        ----------
        p1: tuple or list containing the end position
        p0: tuple or list containing the start position.
            Default is the present position
        draw: boolean, draw a line if True. Default self.draw
        """
        if not p0:
            p0 = self.position
        if draw is None:
            draw = self.draw
        if draw:
            plt.plot((p0[0], p1[0]), (p0[1], p1[1]), color=self.color)
        self.set_position(p1)


    def set_position(self, p):
        self.set_x(p[0])
        self.set_y(p[1])


    def set_x(self, x):
        self.x = float(x)
        self.position[0] = self.x


    def set_y(self, y):
        self.y = float(y)
        self.position[1] = self.y


    def set_draw(self, draw=True):
        """Switch drawing on or off.

        Parameters:
        draw: boolean, Default: True, new draw state
        """
        self.draw = bool(draw)
