from math import copysign,fabs,sin

def findRoot(f,a,b,epsilon):
	m = (b+a)/2
	fa = f(a)
	fb = f(b)
	fm = f(m)
	
	if fabs(b-a)<=epsilon:
		return m
	elif (fa<=0 and fm>=0) or (fa>=0 and fm<=0):
		return findRoot(f,a,m,epsilon)
	elif (fb<=0 and fm>=0) or (fb>=0 and fm<=0):
		return findRoot(f,b,m,epsilon)
	else: return None
	
def findAllRoots(f,a,b,epsilon):
	result = []
	fa = f(a)
	fb = f(a+epsilon)
	m = a+epsilon/2
	for x in range(1,int((b-a)/epsilon)):
		if (fa<=0 and fb>=0) or (fa>=0 and fb<=0):
			result.append(m)
		fa = fb
		fb = f(a+x*epsilon)
		m += epsilon
	return result
		
		