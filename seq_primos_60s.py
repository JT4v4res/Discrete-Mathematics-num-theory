#-*- coding: utf-8 -*-
import numpy
import math
import time, sys

#catching the limit time
end_time = time.time() + 60	

def primao():
	x = 1
	i = 2
	c = 0
	#while the time isn't the limit time
	while time.time() < end_time:
		c = 0
		for i in range(2,x):
			#if the number has another divisor, c is incremented
			if (x % i == 0):
				c += 1
		#if c isn't 0, the number was divided by more numbers than 1 and himself
		if (c == 0):
			print(x)
		x += 1

primao()