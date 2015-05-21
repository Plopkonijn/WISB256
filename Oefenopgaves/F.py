max = int(input())
S = [int(c) for c in input()]
F = 0
T = S[0]

for i in range(1,len(S)):
	if i>T:
		F +=(i-T)
		T +=(i-T)
	T+=S[i]
	
print(F)
	