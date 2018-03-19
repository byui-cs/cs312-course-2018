from matrix import *
from point import *


def testMultiply():
    a = Matrix3([1, -4, -1, 4, 0, 3, -3, 5, 6])
    b = Matrix3([-2, 1, 7, 2, -4, -1, 3, 4, 5])
    c = Matrix3([-2, 1, 7, 2, -4, -1, 3, 4, 5])
    d = a * b
    print('a * b')
    print(d)
	# ----------------------------------
	# |    -13.00      13.00       6.00|
	# |      1.00      16.00      43.00|
	# |     34.00       1.00       4.00|
	# ----------------------------------

    e = a * b * c
    print('a * b * c')
    print(e)
	# ----------------------------------
	# |     70.00     -41.00     -74.00|
	# |    159.00     109.00     206.00|
	# |    -54.00      46.00     257.00|
	# ----------------------------------    


def testAdd():
    a = Matrix3([1, -4, -1, 4, 0, 3, -3, 5, 6])
    b = Matrix3([-2, 1, 7, 2, -4, -1, 3, 4, 5])
    c = a + b
    print('add')
    print(c)
	# ----------------------------------
	# |     -1.00      -3.00       6.00|
	# |      6.00      -4.00       2.00|
	# |      0.00       9.00      11.00|
	# ----------------------------------


def testSub():
    a = Matrix3([1, -4, -1, 4, 0, 3, -3, 5, 6])
    b = Matrix3([-2, 1, 7, 2, -4, -1, 3, 4, 5])
    c = a - b
    print('sub')
    print(c)
	# ----------------------------------
	# |      3.00      -5.00      -8.00|
	# |      2.00       4.00       4.00|
	# |     -6.00       1.00       1.00|
	# ----------------------------------

def testPointMat():
    print('Point * Mat')
    pt = Point(3, 4)
    m = Matrix3([2,0,10, 0,3,20, 0,0,1])
    newPt = pt * m
    print(pt)
    print(m)
    print(newPt)
	# (3.0, 4.0, 1.0)
	# ----------------------------------
	# |      2.00       0.00      10.00|
	# |      0.00       3.00      20.00|
	# |      0.00       0.00       1.00|
	# ----------------------------------    
	# (16.0, 32.0, 1.0)


def main():

	# TODO - get these functions working

	testAdd()
	testSub()
	testMultiply()
	testPointMat()

	# TODO
	# create a final matrix that contains a 
	# - translation of (10, 20)
	# - rotation of 45
	# - scale factor of (0.5, 2)

	# When you print the final matrix will you have the following results:

	print('-------------------------------------------------------------------------')

	s = Matrix3('Identy')
	s.scale(2, 3)

	t = Matrix3('Identy')
	t.translation(10, -10)

	r = Matrix3('Identy')
	r.rotation(-45)

	# TODO - combine all matrices in the right order to rotate, translate and scale a point

	# print(s)
	# print(t)
	# print(r)

	pt = Point(5, 5)

	# Apply combined Matrix to pt

	# Results should be (27.67766952966369, -6.464466094067262, 1.0)


main()

