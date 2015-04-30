import sys
import time

def primes_sieve_S(limit):
	yield 2
	Sieve = [True]*(limit//2)
	Sieve[0] = False
	for j in range(1,(limit-1)//6):
		for i in range(3*j+1,limit//2,2*j+1):
			Sieve[i]=False

	for (i,isprime) in enumerate(Sieve):
		if isprime:
			yield 2*i+1

N = int(sys.argv[1])
T1 = time.time()
primes = list(primes_sieve_S(N))
T2 = time.time()
print('Found', len(primes),'prime numbers smaller than',N,'in',T2-T1,'sec')						
pout = open(sys.argv[2],'w')
for p in primes:
	pout.write(str(p)+'\n')
pout.close()