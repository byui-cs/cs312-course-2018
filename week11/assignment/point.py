# **********************************************************************
# Point Class
# 2018 - Winter
# **********************************************************************

import numpy as np
import math
from matrix import *

##########################################################################
# Module Exceptions

##########################################################################
# global variables and funtions

##########################################################################
# Point class - Simple x and y (and extra)
class Point:
    def __init__(self, x, y):
        self.values = [float(x), float(y), 1.0]

    def __repr__(self):
        return "({}, {}, {})".format(self.values[0], self.values[1], self.values[2])

    def getX(self):
        return self.values[0]

    def getY(self):
        return self.values[1]

    def setX(self, value):
        self.values[0] = value

    def setY(self, value):
        self.values[1] = value

    # Returns a new point from the expression -> Point * Matrix
    def __mul__(self, m):
        tmp = Point(0, 0)
        tmp.setX(m.mat[0][0] * self.getX() + m.mat[0][1] * self.getY() + m.mat[0][2])
        tmp.setY(m.mat[1][0] * self.getX() + m.mat[1][1] * self.getY() + m.mat[1][2])
        return tmp

