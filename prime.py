#-*- coding: utf-8 -*-

x = int(input())
i = 2;
c = 0;

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
	print("É PRIMO")
else:
	print("NÃO É PRIMO")
