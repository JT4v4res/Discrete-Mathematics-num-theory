import numpy
import math

def euclides_algorithm(a, b):
	z = 0
	rMod = 0		
	while rMod == 0 :

		z = b / a
		#catching the division rest
		rMod = b % a

		b = a
		if rMod:
			a = rMod
	return a


x = int(input())
y = int(input())
r = euclides_algorithm(x,y)
str(x)
str(y)
str(r)
print "mdc(",x,",",y,") = ", r