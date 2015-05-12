import math
import random

def drop_needle(L):
	x0 = random.random()
	y0 = random.random()
	phi = random.vonmisesvariate(0,0)
	x1 = x0 + L * math.cos(phi)
	y1 = y0 + L * math.sin(phi)
	if int(y0) !=int(y1):
		return True
	else:
		return False
	
	
	
	
	
count = 1000000
pi = 0
for i in range(count):
	if(drop_needle(1)):
		pi = pi +1
print(count/pi)
print(math.pi)