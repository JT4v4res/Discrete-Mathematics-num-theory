#Python program to calculate the Extended Euclidean Algorithm

def euclidean_extended_algorithm(a, b, x, y):
    if a == 0:
        x = 0
        y = 1
        return b
    x1 = 1
    y1 = 1 #Store the recusive results
    mcd = euclidean_extended_algorithm(b % a, a, x1, y1)
    #updating x and y with the recursive results
    x = y1 - (b / a) * x1
    y = x1
    return mcd

x = 1
y = 1
a = int(input())
b = int(input())
mcd = euclidean_extended_algorithm(a,b,x,y)
print("mcd(",a,", ", b,") = ", mcd, sep='')
