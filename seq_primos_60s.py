#-*- coding: utf-8 -*-
import numpy
import math
import time, sys

end_time = time.time() + 60	

def primao():
	x = 1
	i = 2
	c = 0
	while time.time() < end_time:
		c = 0
		for i in range(2,x):
			if (x % i == 0):
				c += 1
		if (c == 0):
			print(x)
		x += 1

primao()