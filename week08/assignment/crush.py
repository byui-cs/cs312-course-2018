# **********************************************************************
# Crush - CS312 Drawing Engine
# 2018 - Winter
# Refer to https://docs.python.org/2/library/turtle.html#turtle.forward
# for details on the methods you need to implement.s
# **********************************************************************

from graphics import *
import math

##########################################################################
# Module Exceptions

##########################################################################
# global variables and funtions

# Convert degrees to radians
def deg2rad(value):
    return (((math.pi / 180.0) * (value)))

#  Convert radians to degrees
def rad2deg(value):
    return (((value) * (180.0 / math.pi)))

# Range fucntion that uses floating point numbers
def frange(x, y, jump = 1.0):
    while x < y:
        yield x
        x += jump

##########################################################################
# Vec2D class
# This class is used by some of the method in Crush

class Vec2D():

    def __init__(self, x, y = None):
        if (y == None):
            self.x = x.getX()
            self.y = x.getY()
        else:
            self.x = x
            self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, value):
        self.x = value

    def setY(self, value):
        self.y = value

    def getDistance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def getAngle(self):
        return rad2deg(math.atan2(-self.y, self.x))

    def setVector(self, angle, distance):
        angleRadians = deg2rad(angle)
        self.x = math.cos(angleRadians) * distance
        self.y = -math.sin(angleRadians) * distance

    def setDistance(self, distance):
        angleRadians = deg2rad(self.getAngle())
        self.x = -math.cos(angleRadians) * distance
        self.y = -math.sin(angleRadians) * distance

    def setAngle(self, angle):
        angleRadians = deg2rad(angle)
        distance = self.getDistance()
        self.x = math.cos(angleRadians) * distance
        self.y = -math.sin(angleRadians) * distance


############################################################################
# Crush Class
class Crush():

    def __init__(self, title="Graphics Window", width=400, height=400):

        # Create the drawing context
        self.win = GraphWin(title, width, height)

        # TODO - add variables as needed for this project
        self.midX = width / 2.0         # mid point in X
        self.midY = height / 2.0        # mid point in Y

    # --------------------------------------------------------------------------
    # This function will ONLY be called from this class.  Do not call it from
    # any other code in your project.  In python, you can't make methods private.
    # This is the ONLY drawing function that all of your projects will be using
    # to display graphics in the window.
    def _displayPixel(self, x, y, color="black"):
        # print(x + self.midX, y + self.midY, color)
        self.win.plotPixel(x + self.midX, y + self.midY, color)


    # --------------------------------------------------------------------------
    # This function forces any drawing that your program has done to be drawn in
    # the window. Calling this function too many times, will slow down your program
    def flush(self):
        self.win.flush()


    # --------------------------------------------------------------------------
    # Parameters:	distance – a number (integer or float)
    #
    # Move the turtle forward by the specified distance, in the direction the
    # turtle is headed.
    def forward(self, dist):
        pass

    # --------------------------------------------------------------------------
    # Variation of forward()
    def fd(self, dist):
        self.forward(dist)

    # --------------------------------------------------------------------------
    # Parameters:	distance – a number
    #
    # Move the turtle backward by distance, opposite to the direction the turtle
    # is headed. Do not change the turtle’s heading.
    def backward(self, dist):
        pass

    # --------------------------------------------------------------------------
    # Variation of backward()
    def bk(self, dist):
        self.backward(dist)

    # --------------------------------------------------------------------------
    # Parameters:	angle – a number (integer or float)
    #
    # Turn turtle right by angle units. (Units are by default degrees, but can be
    # set via the degrees() and radians() functions.) Angle orientation depends on
    # the turtle mode, see mode().
    def right(self, amount):
        pass

    # --------------------------------------------------------------------------
    # Variation of right()
    def rt(self, amount):
        self.right(amount)

    # --------------------------------------------------------------------------
    # Parameters:	angle – a number (integer or float)
    #
    # Turn turtle left by angle units. (Units are by default degrees, but can be set
    # via the degrees() and radians() functions.) Angle orientation depends on the
    # turtle mode, see mode().
    def left(self, amount):
        pass

    # --------------------------------------------------------------------------
    # Variation of left()
    def lt(self, amount):
        self.left(amount)


    # --------------------------------------------------------------------------
    # Parameters:
    # x – a number or a pair/vector of numbers
    # y – a number or None
    #
    # If y is None, x must be a pair of coordinates or a Vec2D (e.g. as returned by pos()).
    # Move turtle to an absolute position. If the pen is down, draw line. Do not change
    # the turtle’s orientation.
    def goto(self, x, y = None):
        pass


    # --------------------------------------------------------------------------
    # Pull the pen down – drawing when moving.
    def pendown(self):
        pass


    # --------------------------------------------------------------------------
    # Variation of pendown()
    def down(self):
        self.pendown()


    # --------------------------------------------------------------------------
    # Variation of pendown()
    def pd(self):
        self.pendown()

    # --------------------------------------------------------------------------
    # Pull the pen up – no drawing when moving.
    def penup(self):
        pass

    # --------------------------------------------------------------------------
    # Variation of penup()
    def up(self):
        self.penup()

    # --------------------------------------------------------------------------
    # Variation of penup()
    def pu(self):
        self.penup()


    # --------------------------------------------------------------------------
    # Return True if pen is down, False if it’s up.
    def isdown(self):
        pass


    # --------------------------------------------------------------------------
    # Parameters:	x – a number (integer or float)
    #
    # Set the turtle’s first coordinate to x, leave second coordinate unchanged.
    def setx(self, x):
        pass


    # --------------------------------------------------------------------------
    # Parameters:	y – a number (integer or float)
    #
    # Set the turtle’s second coordinate to y, leave first coordinate unchanged.
    def sety(self, y):
        pass


    # --------------------------------------------------------------------------
    # Move turtle to the origin – coordinates (0,0) – and set its heading to its
    # start-orientation.
    def home(self):
        pass


    # --------------------------------------------------------------------------
    # Parameters:	to_angle – a number (integer or float)
    #
    # Set the orientation of the turtle to to_angle in degrees.
    def setheading(self, heading):
        pass


    # --------------------------------------------------------------------------
    # Variation of setheading()
    def seth(self, heading):
        self.setheading(heading)


    # --------------------------------------------------------------------------
    # Parameters:
    # size – an integer >= 1 (if given)
    # color – a colorstring or a numeric color tuple
    #
    # Draw a circular dot with diameter size, using color.
    def dot(self, size=1, color='black'):
        pass


    # --------------------------------------------------------------------------
    # Return the turtle’s current location (x,y) (as a Vec2D vector).
    def position(self):
        pass

    # --------------------------------------------------------------------------
    # Variation of position()
    def pos(self):
        return self.position()


    # --------------------------------------------------------------------------
    # Return the turtle’s x coordinate.
    def xcor(self):
        pass


    # --------------------------------------------------------------------------
    # Return the turtle’s y coordinate.
    def ycor(self):
        pass


    # --------------------------------------------------------------------------
    # Return the turtle’s current heading.
    def heading(self):
        pass


    # --------------------------------------------------------------------------
    # print() formatting
    def __str__(self):
        # TODO - This function is called by the Python print() function, add what you want
        return 'Crush display TODO'


    # ##########################################################################
    # The following functions are here to help interacting with the user in the
    # main screen.

    # --------------------------------------------------------------------------
    # Get the position where the mouse was clicked in the window
    def getMouse(self):
        return self.win.getMouse()

    # --------------------------------------------------------------------------
    # Return last mouse click or None if mouse has not been clicked since last call
    def checkMouse(self):
        return self.win.checkMouse()

    # --------------------------------------------------------------------------
    # Wait for user to press a key and return it as a string
    def getKey(self):
        return self.win.getKey()

    # --------------------------------------------------------------------------
    # Return last key pressed or None if no key pressed since last call
    def checkKey(self):
        return self.win.checkKey()

    # --------------------------------------------------------------------------
    # Return the height of the window
    def getHeight(self):
        return self.height

    # --------------------------------------------------------------------------
    # Return the width of the window
    def getWidth(self):
        return self.width

    # --------------------------------------------------------------------------
    # Define your own mouse handler function
    def setMouseHandler(self, func):
        self.win.setMouseHandler(func)

    # --------------------------------------------------------------------------
    # Call this to finish any program that you use Crush
    def close(self):
        self.win.close()
