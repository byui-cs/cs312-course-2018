# graphics.py
# **********************************************************************
# grpahics - Drawing Context
# 2018 - Winter
# Don't change this code
# **********************************************************************

import time, os, sys

# try:  # import as appropriate for 2.x vs. 3.x
#    import tkinter as tk
# except:
#    import Tkinter as tk

import tkinter as tk

##########################################################################
# Module Exceptions

class GraphicsError(Exception):
    """Generic error class for graphics module exceptions."""
    pass

OBJ_ALREADY_DRAWN = "Object currently drawn"
UNSUPPORTED_METHOD = "Object doesn't supprt operation"
BAD_OPTION = "Illegal option value"

##########################################################################
# global variables and funtions

_root = tk.Tk()
_root.withdraw()

############################################################################
# Graphics classes start here
class GraphWin(tk.Canvas):

    def __init__(self, title="Graphics Window", width=400, height=400):
        assert type(title) == type(""), "Title must be a string"
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master, width=width, height=height, highlightthickness=0, bd=0)
        self.master.title(title)
        self.pack()
        master.resizable(0,0)
        self.foreground = "black"
        self.mouseX = None
        self.mouseY = None
        self.bind("<Button-1>", self._onClick)
        self.bind_all("<Key>", self._onKey)
        self.height = int(height)
        self.width = int(width)
        self.autoflush = False
        self._mouseCallback = None
        self.closed = False
        master.lift()
        self.lastKey = ""
        self.flush


    def __repr__(self):
        if self.isClosed():
            return "<Closed GraphWin>"
        else:
            return "GraphWin('{}', {}, {})".format(self.master.title(),
                                             self.getWidth(),
                                             self.getHeight())


    def __str__(self):
        return repr(self)
     

    def __checkOpen(self):
        if self.closed:
            raise GraphicsError("window is closed")


    def _onKey(self, evnt):
        self.lastKey = evnt.keysym


    def setBackground(self, color):
        """Set background color of the window"""
        self.__checkOpen()
        self.config(bg=color)
        self.__autoflush()


    def close(self):
        """Close the window"""

        if self.closed: return
        self.closed = True
        self.master.destroy()
        self.__autoflush()


    def isClosed(self):
        return self.closed


    def isOpen(self):
        return not self.closed


    def __autoflush(self):
        if self.autoflush:
            _root.update()


    def plotPixel(self, x, y, color="black"):
        """Set pixel raw (independent of window coordinates) pixel
        (x,y) to color"""
        self.__checkOpen()
        self.create_line(x,y,x+1,y, fill=color)
        # self.__autoflush()


    def flush(self):
        """Update drawing to the window"""
        self.__checkOpen()
        _root.update()


    def getMouse(self):
        """Wait for mouse click and return Point object representing
        the click"""
        self.update()      # flush any prior clicks
        self.mouseX = None
        self.mouseY = None
        while self.mouseX == None or self.mouseY == None:
            self.update()
            if self.isClosed(): raise GraphicsError("getMouse in closed window")
            time.sleep(.1) # give up thread
        x,y = self.mouseX, self.mouseY
        self.mouseX = None
        self.mouseY = None
        return Point(x,y)


    def checkMouse(self):
        """Return last mouse click or None if mouse has
        not been clicked since last call"""
        if self.isClosed():
            raise GraphicsError("checkMouse in closed window")
        self.update()
        if self.mouseX != None and self.mouseY != None:
            x,y = self.mouseX, self.mouseY
            self.mouseX = None
            self.mouseY = None
            return Point(x,y)
        else:
            return None


    def getKey(self):
        """Wait for user to press a key and return it as a string."""
        self.lastKey = ""
        while self.lastKey == "":
            self.update()
            if self.isClosed(): raise GraphicsError("getKey in closed window")
            time.sleep(.1) # give up thread

        key = self.lastKey
        self.lastKey = ""
        return key


    def checkKey(self):
        """Return last key pressed or None if no key pressed since last call"""
        if self.isClosed():
            raise GraphicsError("checkKey in closed window")
        self.update()
        key = self.lastKey
        self.lastKey = ""
        return key


    def getHeight(self):
        """Return the height of the window"""
        return self.height


    def getWidth(self):
        """Return the width of the window"""
        return self.width
    

    def setMouseHandler(self, func):
        self._mouseCallback = func


    def _onClick(self, e):
        self.mouseX = e.x
        self.mouseY = e.y
        if self._mouseCallback:
            self._mouseCallback(Point(e.x, e.y))


############################################################################
# Point class - Simple x and y
class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)
        
    def getX(self): return self.x
    def getY(self): return self.y


############################################################################
def color_rgb(r,g,b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color"""
    return "#%02x%02x%02x" % (r,g,b)


# MacOS fix 1
# update()
