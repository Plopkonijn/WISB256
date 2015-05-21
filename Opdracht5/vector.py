from array import array
from math import sqrt
class Vector:
	def __init__(self,n,value=0):
		if type(value)==int or type(value) == float:
			self.v = array('d',[value]*n)
		else:
			self.v = array('d',value)

	def __str__(self):
		result = ''
		for x in self.v:
			result += str(x) + '\n'
		return result[:-1]
	
	def lincomb(self,other,alpha,beta):
		result = []
		for i in range(len(self.v)):
			result.append(self.v[i]*alpha + other.v[i] * beta)
		return Vector(len(result),result)
	
	def scalar(self,alpha):
		result = []
		for i in range(len(self.v)):
			result.append(self.v[i]*alpha)
		return Vector(len(result),result)
	
	def inner(self,other):
		result = 0
		for i in range(len(self.v)):
			result += self.v[i]*other.v[i]
		return result
		
	def norm(self):
		result = 0
		for i in range(len(self.v)):
			result += self.v[i]**2
		return sqrt(result)
		
def GrammSchmidt(vectors):
	result = []
	for v in vectors:
		u = v
		for w in result:
			u = u.lincomb(w.scalar(w.inner(v)/w.inner(w)),1,-1)
		result.append(u.scalar(1/u.norm()))
	
	return result

v0 = Vector(2,[3,1])
v1 = Vector(2,[2,2])
W = GrammSchmidt([v0,v1])
print(W[0])

print(W[1])
			
print(W[0].inner(W[1]))

print(W[0].norm())

print(W[1].norm())
		
	
	
	
