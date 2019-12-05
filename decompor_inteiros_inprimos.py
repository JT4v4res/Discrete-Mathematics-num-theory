#-*- coding: utf-8 -*-
import numpy
from math import sqrt

def decomp(n):
	"""Finds the prime factors of 'n'"""
	pFact, limit, cheking, number = [], int(sqrt(n)) + 1, 2, n
	#Verifying if the number is 1
	if n == 1: 
		return [1]
	for checking in range(2,limit):
		#While the number is divible by that prime number...
		while number % checking == 0:
			#Adding the prime in the end of the list
			pFact.append(checking)
			#Going to the next number to see he's primes factors
			number /= check
		#If the number is greater than 1, he's added to the list end
		if number > 1:
			pFact.append(number)
		#returning the list with factors
		return pFact

i = int(input())
print decomp(i)