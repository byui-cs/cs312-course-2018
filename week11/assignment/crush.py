# **********************************************************************
# Crush - CS312 Drawing Engine
# 2018 - Winter
# Refer to https://docs.python.org/2/library/turtle.html#turtle.forward
# for details on the methods you need to implement.s
# **********************************************************************

from graphics import *
from matrix import *
from point import *
from common import *
import math

##########################################################################
# Module Exceptions

##########################################################################
# global variables and funtions


##########################################################################
# Vec2D class
# This class is used by some of the method in Crush

class Vec2D():

    def __init__(self, x, y = None):
        if (y == None):
            self.dx = x.getDx()
            self.dy = x.getDy()
        else:
            self.dx = x
            self.dy = y

    def getDx(self):
        return self.dx

    def getDy(self):
        return self.dy

    def setX(self, value):
        self.dx = value

    def setY(self, value):
        self.dy = value

    def getDistance(self):
        return math.sqrt(self.dx * self.dx + self.dy * self.dy)

    def getAngle(self):
        return rad2deg(math.atan2(-self.dy, self.dx))

    def _setXY(self, radians, dist):
        self.dx = math.cos(radians) * dist
        self.dy = -math.sin(radians) * dist

    def setVector(self, angle, distance):
        self._setXY(deg2rad(angle), distance)

    def setDistance(self, distance):
        self._setXY(deg2rad(self.getAngle()), distance)

    def setAngle(self, angle):
        self._setXY(deg2rad(angle), self.getDistance())


############################################################################
# Crush Class
class Crush():

    def __init__(self, title="Graphics Window", width=400, height=400):

        # Create the drawing context
        self.win = GraphWin(title, width, height)

        # TODO - add variables as needed for projects

        # Current position of Crush
        self.pos = Point(0, 0)

        self.head = 0.0
        self.width = width
        self.height = height

        # TODO Project 11: Add your matrices here
        pass


    def createCombinedMatrix(self):
    	# TODO Project 11: Impliment this function
    	pass


    # Set the rotation matrix
    def rotation(self, rot):
    	# TODO Project 11: Impliment this function (This function returns nothing)
    	pass


    # Set the scale matrix
    def scale(self, x, y):
    	# TODO Project 11: Impliment this function  (This function returns nothing)
    	pass


    # Set the translation matrix
    def translate(self, x, y):
    	# TODO Project 11: Impliment this function  (This function returns nothing)
    	pass


    def _plotLineLow(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy

        D = 2*dy - dx
        y = y0

        for x in frange(x0, x1):
            self._displayPixel(x, y)
            if D > 0:
                y = y + yi
                D = D - 2*dx
            D = D + 2*dy


    def _plotLineHigh(self, x0,y0, x1,y1):
        dx = x1 - x0
        dy = y1 - y0
        xi = 1
        if dx < 0:
            xi = -1
            dx = -dx
        D = 2*dx - dy
        x = x0

        for y in frange(y0, y1):
            self._displayPixel(x,y)
            if D > 0:
                x = x + xi
                D = D - 2*dy
            D = D + 2*dx

    def _plotLine(self, x0,y0, x1,y1):
        if math.fabs(y1 - y0) < math.fabs(x1 - x0):
            if x0 > x1:
                self._plotLineLow(x1, y1, x0, y0)
            else:
                self._plotLineLow(x0, y0, x1, y1)
        else:
            if y0 > y1:
                self._plotLineHigh(x1, y1, x0, y0)
            else:
                self._plotLineHigh(x0, y0, x1, y1)


    # --------------------------------------------------------------------------
    # This function will ONLY be called from this class.  Do not call it from
    # any other code in your project.  In python, you can't make methods private.
    # This is the ONLY drawing function that all of your projects will be using
    # to display graphics in the window.
    def _displayPixel(self, x, y, color="black"):
        self.win.plotPixel(x, y, color)

	# Helper function for floodfill
    def _addToFloodStack(self, stack, r, c):
        pt = Point(r, c)
        pt2 = pt * self.createCombinedMatrix()

        if (pt2.getX() >= self.width): return
        if (pt2.getY() >= self.height): return
        if (pt2.getX() <= 0): return
        if (pt2.getY() <= 0): return

        if (self.win.isPixelOn(pt2.getX(), pt2.getY()) == False):
            stack.append((r, c))

    # --------------------------------------------------------------------------
    # This function will fill an area using 4 directional fill alogrithm
    # The self.win object has the methods:
    #     isPixelOn()
    #     clearWindow()
    def floodfill(self, x, y, color='black'):
        stack = [(x, y)]
        count = 0
        self._addToFloodStack(stack, x, y)
        while (len(stack) > 0):
            # pop a point
            r, c = stack.pop()
            # print(r, c, self.pos)

            if (self.win.isPixelOn(r, c) == False):
                self._displayPixel(r, c, color)
                count += 1
                if (count % 3000 == 0):
                    self.flush()

                # push on stack
                self._addToFloodStack(stack, r + 1, c)
                self._addToFloodStack(stack, r - 1, c)
                self._addToFloodStack(stack, r, c + 1)
                self._addToFloodStack(stack, r, c - 1)


    # --------------------------------------------------------------------------
    # This function forces any drawing that your program has done to be drawn in
    # the window
    # Calling this function too many times, will slow down your program
    def flush(self):
        self.win.flush()


    # --------------------------------------------------------------------------
    # Parameters:	distance – a number (integer or float)
    #
    # Move the turtle forward by the specified distance, in the direction the
    # turtle is headed.
    def forward(self, dist):
        x1 = self.pos.getX()
        y1 = self.pos.getY()

        newVec = Vec2D(0, 0)
        newVec.setVector(self.head, dist)

        x2 = x1 + newVec.getDx()
        y2 = y1 + newVec.getDy()

        # Apply matrix
        p0 = Point(x1, y1) * self.createCombinedMatrix()
        p1 = Point(x2, y2) * self.createCombinedMatrix()

        self._plotLine(p0.getX(), p0.getY(), p1.getX(), p1.getY())

        self.pos.setX(x2)
        self.pos.setY(y2)

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
        self.forward(-dist)

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
        self.head -= amount

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
        self.head += amount

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
        self.pos.setX(x)
        self.pos.setY(y)


    # --------------------------------------------------------------------------
    # Parameters:	x – a number (integer or float)
    #
    # Set the turtle’s first coordinate to x, leave second coordinate unchanged.
    def setx(self, x):
        self.pos.setX(x)


    # --------------------------------------------------------------------------
    # Parameters:	y – a number (integer or float)
    #
    # Set the turtle’s second coordinate to y, leave first coordinate unchanged.
    def sety(self, y):
        self.pos.setY(y)


    # --------------------------------------------------------------------------
    # Move turtle to the origin – coordinates (0,0) – and set its heading to its
    # start-orientation (which depends on the mode, see mode()).
    def home(self):
        self.pos.setX(0)
        self.pos.setY(0)


    # --------------------------------------------------------------------------
    # Parameters:	to_angle – a number (integer or float)
    #
    # Set the orientation of the turtle to to_angle. Depends on the degree/radians mode
    def setheading(self, heading):
        self.head = heading


    # --------------------------------------------------------------------------
    # Variation of setheading()
    def seth(self, heading):
        self.setheading(heading)


    # --------------------------------------------------------------------------
    # Parameters:
    # color – a colorstring or a numeric color tuple
    #
    # Draw a dot
    def dot(self, color='black'):
        self._displayPixel(self.pos.getX(), self.pos.getY(), color)

    # --------------------------------------------------------------------------
    # Parameters:	speed – an integer in the range 0..10 or a speedstring (see below)
    #
    # Set the turtle’s speed to an integer value in the range 0..10. If no argument
    # is given, return current speed.
    #
    # If input is a number greater than 10 or smaller than 0.5, speed is set to 0.
    # Speedstrings are mapped to speedvalues as follows:
    #
    # “fastest”: 0
    # “fast”: 10
    # “normal”: 6
    # “slow”: 3
    # “slowest”: 1
    # Speeds from 1 to 10 enforce increasingly faster animation of line drawing and
    # turtle turning.
    #
    # Attention: speed = 0 means that no animation takes place. forward/back makes
    # turtle jump and likewise left/right make the turtle turn instantly.
    def speed(self):
        pass


    # --------------------------------------------------------------------------
    # Return the turtle’s current location (x,y) (as a Vec2D vector).
    def position(self):
        return self.pos

    # --------------------------------------------------------------------------
    # Variation of position()
    def pos(self):
        return self.position()


    # --------------------------------------------------------------------------
    # Parameters:
    # x – a number or a pair/vector of numbers or a turtle instance
    # y – a number if x is a number, else None
    #
    # Return the angle between the line from turtle position to position specified
    # by (x,y), the vector or the other turtle. This depends on the turtle’s start
    # orientation which depends on the mode - “standard”/”world” or “logo”).
    def towards(self, x, y = None):
        pass


    # --------------------------------------------------------------------------
    # Return the turtle’s x coordinate.
    def xcor(self):
        return self.pos.getX()


    # --------------------------------------------------------------------------
    # Return the turtle’s y coordinate.
    def ycor(self):
        return self.pos.getY()


    # --------------------------------------------------------------------------
    # Return the turtle’s current heading
    def heading(self):
        return self.head


    # --------------------------------------------------------------------------
    # Parameters:
    # x – a number or a pair/vector of numbers or a turtle instance
    # y – a number if x is a number, else None
    #
    # Return the distance from the turtle to (x,y), the given vector, or the given
    # other turtle, in turtle step units.
    def distance(self, x, y = None):
        pass


    # --------------------------------------------------------------------------
    # Parameters:	deg – a number
    # Set angle measurement units, i.e. set number of “degrees” for a full circle.
    # Default value is 360 degrees.
    def degrees(self, deg = 360.0):
        pass


    # --------------------------------------------------------------------------
    # Set the angle measurement units to radians. Equivalent to degrees(2*math.pi).
    def radians(self):
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
    # Return the current pencolor and the current fillcolor as a pair of color
    # specification strings or tuples as returned by pencolor() and fillcolor().
    # color(colorstring), color((r,g,b)), color(r,g,b)
    # Inputs as in pencolor(), set both, fillcolor and pencolor, to the given value.
    # color(colorstring1, colorstring2), color((r1,g1,b1), (r2,g2,b2))
    # Equivalent to pencolor(colorstring1) and fillcolor(colorstring2) and analogously
    # if the other input format is used.
    # If turtleshape is a polygon, outline and interior of that polygon is drawn with
    # the newly set colors.
    def color(self):
        pass


    # --------------------------------------------------------------------------
    # Return or set the pencolor. Four input formats are allowed:
    #
    # pencolor()
    # Return the current pencolor as color specification string or as a tuple
    # May be used as input to another color/pencolor/fillcolor call.
    #
    # pencolor(colorstring)
    # Set pencolor to colorstring, which is a Tk color specification string,
    # such as "red", "yellow", or "#33cc8c".
    #
    # pencolor((r, g, b))
    # Set pencolor to the RGB color represented by the tuple of r, g, and b.
    # Each of r, g, and b must be in the range 0..colormode, where colormode
    # is either 1.0 or 255 (see colormode()).
    #
    # pencolor(r, g, b)
    # Set pencolor to the RGB color represented by r, g, and b. Each of r, g,
    # and b must be in the range 0..colormode.
    #
    # If turtleshape is a polygon, the outline of that polygon is drawn with
    # the newly set pencolor.
    def pencolor(self, *args):
        pass


    # --------------------------------------------------------------------------
    # Return or set the fillcolor. Four input formats are allowed:
    #
    # fillcolor()
    # Return the current fillcolor as color specification string, possibly in tuple
    # format (see example). May be used as input to another color/pencolor/fillcolor call.
    #
    # fillcolor(colorstring)
    # Set fillcolor to colorstring, which is a Tk color specification string,
    # such as "red", "yellow", or "#33cc8c".
    #
    # fillcolor((r, g, b))
    # Set fillcolor to the RGB color represented by the tuple of r, g, and b.
    # Each of r, g, and b must be in the range 0..colormode, where colormode
    # is either 1.0 or 255 (see colormode()).
    #
    # fillcolor(r, g, b)
    # Set fillcolor to the RGB color represented by r, g, and b. Each of r, g,
    # and b must be in the range 0..colormode.
    #
    # If turtleshape is a polygon, the interior of that polygon is drawn with
    # the newly set fillcolor.
    def fillcolor(self, *args):
        pass


    # --------------------------------------------------------------------------
    # Parameters:	flag – True/False (or 1/0 respectively)
    #
    # Call fill(True) before drawing the shape you want to fill, and fill(False)
    # when done. When used without argument: return fillstate
    # (True if filling, False else).
    def fill(self):
        pass


    # --------------------------------------------------------------------------
    # Call just before drawing a shape to be filled. Equivalent to fill(True).
    def begin_fill(self):
        pass


    # --------------------------------------------------------------------------
    # Fill the shape drawn after the last call to begin_fill(). Equivalent to fill(False).
    def end_fill(self):
        pass


    # --------------------------------------------------------------------------
    # Delete the turtle’s drawings from the screen, re-center the turtle and set
    # variables to the default values.
    def reset(self):
        pass


    # --------------------------------------------------------------------------
    # Delete the turtle’s drawings from the screen. Do not move turtle. State and
    # position of the turtle as well as drawings of other turtles are not affected.
    def clear(self):
        pass


    # --------------------------------------------------------------------------
    # Make the turtle invisible. It’s a good idea to do this while you’re in the
    # middle of doing some complex drawing, because hiding the turtle speeds up
    # the drawing observably.
    def showcrush(self):
        pass


    # --------------------------------------------------------------------------
    # Make the turtle visible.
    def hidecrush(self):
        pass


    # --------------------------------------------------------------------------
    # Return True if the Turtle is shown, False if it’s hidden.
    def isvisible(self):
        pass


    # --------------------------------------------------------------------------
    # Parameters:	mode – one of the strings “standard”, “logo” or “world”
    #
    # Set turtle mode (“standard”, “logo” or “world”) and perform reset. If mode
    # is not given, current mode is returned.
    #
    # Mode “standard” is compatible with old turtle. Mode “logo” is compatible
    # with most Logo turtle graphics. Mode “world” uses user-defined “world coordinates”.
    # Attention: in this mode angles appear distorted if x/y unit-ratio doesn’t equal 1.
    #
    # Mode	Initial turtle heading	positive angles
    # “standard”    to the right (east)    counterclockwise
    # “logo”        upward (north)         clockwise
    def mode(self):
        pass



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
    # print() formatting
    def __str__(self):
        # TODO - This function is called by the Python print() function, add what you want
        return 'Crush display TODO'

    # --------------------------------------------------------------------------
    # Call this to finish any program that you use Crush
    def close(self):
        self.win.close()
