def euclidean_algorithm(a, b):		
	while b != 0 :
		a, b = b, a % b
	return a

x = int(input())
y = int(input())
r = euclidean_algorithm(x,y)
print("mdc(",str(x),",",str(y),") = ", str(r))
