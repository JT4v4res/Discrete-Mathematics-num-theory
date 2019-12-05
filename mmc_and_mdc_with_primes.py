# -*- coding: utf-8 -*-
import math
import numpy

def mdc(a, b):
	rest = None
	while rest != 0:
		rest = a % b
		a = b
		b = rest
	return a


# Function mmc
def mmc(n, n2):
	a = n
	b = n2
	#initializing rest
	rest = None
	while rest is not 0:
		rest = a % b
		a  = b
		b  = rest

	return (n * n2) / a

x = int(input())
y = int(input())
rMmc = mmc(x,y)
rMdc = mdc(x,y)
print "mmc(",x,",",y,") = ", rMmc
print "mdc(",x,",",y,") = ", rMdc