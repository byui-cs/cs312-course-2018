# common.py
# **********************************************************************
# common functions
# 2018 - Winter
# Don't change this code
# **********************************************************************

import math

############################################################################
def color_rgb(r,g,b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color"""
    return "#%02x%02x%02x" % (r,g,b)


############################################################################
def deg2rad(value):
    return (((math.pi / 180.0) * (value)))


############################################################################
def rad2deg(value):
    return (((value) * (180.0 / math.pi)))


############################################################################
def frange(x, y, jump = 1.0):
    while x < y:
        yield x
        x += jump

