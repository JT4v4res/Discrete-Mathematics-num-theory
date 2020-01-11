#-*- coding: utf-8 -*-
import numpy
import math
import time, sys

#catching the limit time
end_time = time.time() + 60	

def is_prime():
	x = 1
	i = 2
	c = 0
	#while the time isn't the limit time
	while time.time() < end_time:
		c = 0
		for i in range(2,x):
		  if x == 2:
		    break
		  elif x % 2 == 0:
		    c += 1
		    break
		  elif x % i == 0:
		    c += 1
		    break
		if (c == 0):
			print(x)
		x += 1

is_prime()
