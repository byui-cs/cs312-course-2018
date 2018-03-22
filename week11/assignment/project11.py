# Import the graphics code that will allow us to draw in a window
from crush import *
from matrix import *
from point import *

width = 685
height = 480
wMid = width // 2
hMid = height // 2

# -----------------------------------------------------------------------------
# Draw a rect given the (x, y) and width and height
def drawRect(cr, x, y, w, h):
    cr.penup()
    cr.goto(x, y)
    cr.pendown()
    cr.setheading(0)
    cr.forward(w)
    cr.right(90)
    cr.forward(h)
    cr.right(90)
    cr.forward(w)
    cr.right(90)
    cr.forward(h)

# -----------------------------------------------------------------------------
# draw a rect
def draw_rectangle(cr, length, height, x=0, y=0):
    cr.penup()
    cr.goto(x, y)
    cr.pendown()
    for i in range(2):
        cr.forward(length)
        cr.right(90)
        cr.forward(height)
        cr.right(90)
    cr.setx(length)


# -----------------------------------------------------------------------------
# draw a star
def draw_star(cr, size, x=0, y=0):
    cr.penup()
    cr.goto(x, y)
    cr.down()
    cr.setheading(0)
    side = (size / 2) * 0.7264
    for i in range(5):
        cr.forward(side)
        cr.left(72)
        cr.forward(side)
        cr.right(144)

# -----------------------------------------------------------------------------
# Draw the flag outline
def draw_flag(cr, height):
    fly = 1.9 * float(height)
    hoist_canton = height * (7 / 13)
    fly_canton = fly * (2 / 5)
    stripe = height / 13
    star = int(stripe + 1) # * (4 / 5)
    e = hoist_canton / 10
    f = fly_canton / 14
    draw_rectangle(cr, fly, height)
    draw_rectangle(cr, fly_canton, hoist_canton)

    draw_rectangle(cr, fly - fly_canton, stripe, fly_canton, stripe)
    draw_rectangle(cr, fly - fly_canton, stripe, fly_canton, stripe * 2)
    draw_rectangle(cr, fly - fly_canton, stripe, fly_canton, stripe * 3)
    draw_rectangle(cr, fly - fly_canton, stripe, fly_canton, stripe * 4)
    draw_rectangle(cr, fly - fly_canton, stripe, fly_canton, stripe * 5)
    draw_rectangle(cr, fly - fly_canton, stripe, fly_canton, stripe * 6)

    draw_rectangle(cr, fly, stripe, 0, hoist_canton)
    draw_rectangle(cr, fly, stripe, 0, hoist_canton + (stripe))
    draw_rectangle(cr, fly, stripe, 0, hoist_canton + (stripe * 2))
    draw_rectangle(cr, fly, stripe, 0, hoist_canton + (stripe * 3))
    draw_rectangle(cr, fly, stripe, 0, hoist_canton + (stripe * 4))
    draw_rectangle(cr, fly, stripe, 0, hoist_canton + (stripe * 5))

    for i in range(1, 12, 2):
        for j in range(1, 10, 2):
            draw_star(cr, star, e * i + 6, f * j - 3)

    for i in range(2, 12, 2):
        for j in range(2, 10, 2):
            draw_star(cr, star, e * i + 6, f * j - 3)

# -----------------------------------------------------------------------------
# draw the US flag
def drawFlag(cr, x, y):
    cr.translate(x, y)
    draw_flag(cr, 100)

# -----------------------------------------------------------------------------
def main():

    cr = Crush("test", 600, 500)

	# #########################################################################
	# #########################################################################
	# #########################################################################
    #                 DO NOT CHANGE THIS CODE FOR THE PROJECT
	# #########################################################################
	# #########################################################################
	# #########################################################################

    # Display flags scaled and rotated around the center of the window
    cr.scale(1.3, 0.6)
    for i in range(0, 360, 45):
        cr.rotation(i)
        drawFlag(cr, 300, 250)
        cr.flush()

    # Display stars in a column where each star is rotated
    # Note: the stars need to be in a column (up and down) one after another
    cr.scale(1, 0.5)
    for i in range(20, 170, 35):
        cr.rotation(i)
        cr.translate(40, i)
        draw_star(cr, 50, 0, 0)

    print('Done')

    cr.getMouse() # pause for click in window
    cr.close()

main()

