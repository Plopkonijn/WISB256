class Dice(object):
	
	def __init__(self):
		self.dice = [i for i in range(6)]
	
	def omhoog(self):
		tmp = self.dice[0]
		self.dice[0] = self.dice[2]
		self.dice[2] = self.dice[5]
		self.dice[5] = self.dice[3]
		self.dice[3] = tmp
			
	def omlaag(self):
		tmp = self.dice[0]
		self.dice[0] = self.dice[3]
		self.dice[3] = self.dice[5]
		self.dice[5] = self.dice[2]
		self.dice[2] = tmp
	
	def links(self):
		tmp = self.dice[0]
		self.dice[0] = self.dice[1]
		self.dice[1] = self.dice[5]
		self.dice[5] = self.dice[4]
		self.dice[4] = tmp
			
	def rechts(self):
		tmp = self.dice[0]
		self.dice[0] = self.dice[4]
		self.dice[4] = self.dice[5]
		self.dice[5] = self.dice[1]
		self.dice[1] = tmp
		
	def top(self):
		return int(self.dice[5])+1
		
		
dobbel = Dice()
roles = int(input())
for i in range(roles):
	role = input()
	if role =='omhoog':
		dobbel.omhoog()
	if role =='omlaag':
		dobbel.omlaag()
	if role =='links':
		dobbel.links()
	if role =='rechts':
		dobbel.rechts()
		
print(dobbel.top())