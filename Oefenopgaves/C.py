from math import asin

V = int(input())
G = int(input())
S = int(input())

result = G*S/(V**2)
result = asin(result)/2
result = "{0:.2f}".format(result)
print(result)
