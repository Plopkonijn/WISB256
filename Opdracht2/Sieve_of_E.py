import sys
import math
import time
N = int(sys.argv[1])

T1 = time.time()
sN = int(math.sqrt(N))+1
primes = {i for i in range(3,N,2)}

for i in range(3,sN):
	if i in primes:
		for j in range(i*i,N,2*i):
			try:
				primes.remove(j)
			except:
				pass
T2 = time.time()
print('Found', len(primes),'prime numbers smaller than',N,'in',T2-T1,'sec')		
primes = [p for p in primes]
primes.sort()				

pout = open(sys.argv[2],'w')
pout.write('2\n')
for p in primes:
	pout.write(str(p)+'\n')
pout.close()