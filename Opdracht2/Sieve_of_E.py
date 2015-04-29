import sys
import math
import time
N = int(sys.argv[1])

T1 = time.time()
sN = int(math.sqrt(N))+1
Sieve = [False] + [True] * (N>>1)
primes = [2]
for i in range(3,sN,2):
	print('\ni:',i,Sieve[i//2])
	if Sieve[i//2]:
		for j in range(i*i,N,i<<1):
			print('j:',j,Sieve[j//2])
			Sieve[j//2]=False
T2 = time.time()
print('Found', len(primes),'prime numbers smaller than',N,'in',T2-T1,'sec')		

for i in range(len(Sieve)):
	print(i, 1 + (i<<1), Sieve[i//2])
	if Sieve[i//2]:
		primes.append(1+ i<<1)

pout = open(sys.argv[2],'w')

for p in primes:
	pout.write(str(p)+'\n')
pout.close()