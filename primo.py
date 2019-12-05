#-*- coding: utf-8 -*-
import math
import numpy

x = int(input())
i = 2;
c = 0;
for i in range(2,x):
	if (x % i == 0):
		c += 1
if (c == 0):
	print("É PRIMO")
else:
	print("NÃO É PRIMO")