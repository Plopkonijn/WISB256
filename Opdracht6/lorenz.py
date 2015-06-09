from scipy.integrate import odeint
from scipy.linalg import eig
from numpy import arange,array

class Lorenz:
	def __init__(self,y,p=[10,28,8/3]):
		self.y0 = y
		self.s = p[0]
		self.p = p[1]
		self.b = p[2]
	
	def f(self,yy,t):
		return array([self.s*(yy[0]-yy[1]),yy[0]*(self.p-yy[2])-yy[1],yy[0]*yy[1]-self.b*yy[2]])
	
	def df(self,u):
		return array([[-self.s,self.p-u[2],u[1]],[self.s,-1,u[0]],[0,-u[0],-self.b]])
	
	def solve(self,T,dt):
		t = arange(0,T,dt)
		yy = odeint(self.f,self.y0,t,Dfun=self.df)
		return yy

	def isStable(self,u):
		w,v = eig(self.df(u))
		for i in w:
			if i.real >=0:
				return False
		return True