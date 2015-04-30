import sys
import math

twincount = 0
pin = open(sys.argv[1])

primes = [int(i) for i in pin.read().split()]
for p in range(len(primes)-1):
	if primes[p] +2 == primes[p+1]:
		twincount = twincount+1
N = primes[-1]
C2 = 0.6601618
pi = len(primes)
nlogn = N/(math.log(N))
ratio = pi/nlogn
print('Largest Prime =',N)
print('-'*20)
print('pi(N)         =',pi)
print('N/log(N)      =',nlogn)
print('ratrio        =',ratio)
print('-'*20)
pi =  twincount
nlogn = (C2*2*N)/(math.log(N)**2))
ratio = pi/nlogn
print('pi_2(N)       =',twincount)
print('2CN/log(N)^2  =',nlogn)
print('ratio         =',ratio)
#print(primes)
