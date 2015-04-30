import sys
import time

def primes_sieve_E(limit):
	Sieve = [True] * (limit//2)
	Sieve[0] = False
	yield 2
	for (i,isprime) in enumerate(Sieve):
		if isprime:
			yield (2*i)+1
			for j in range((2*i+1)**2,limit,2*(2*i+1)):
				Sieve[j//2] = False

N = int(sys.argv[1])
T1 = time.time()
primes = list(primes_sieve_E(N))
T2 = time.time()
print('Found', len(primes),'prime numbers smaller than',N,'in',T2-T1,'sec')						
pout = open(sys.argv[2],'w')
for p in primes:
	pout.write(str(p)+'\n')
pout.close()