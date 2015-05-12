from math import pi, cos, sqrt, asin
from random import uniform, seed
import sys

def drop_needle(L):
	x = uniform(0,.5)
	phi = uniform(0,pi/2)
	xtip = x - L*cos(phi)/2
	if xtip <0: 
		return True
	return False
		
N = int(sys.argv[1])
L = float(sys.argv[2])
if len(sys.argv)>3:	seed(int(sys.argv[3]))
C = 0

for i in range(N):
	if drop_needle(L): C+=1
	
print(C,'hits in',N,'tries')
C = C/N
PI = 2*L/C	
if(L>1):PI = 2*(L - sqrt(L*L-1) - asin(1/L))/(C-1)
print('Pi =',PI)
