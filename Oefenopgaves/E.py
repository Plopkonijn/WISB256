def TicTacToe(B):
	for i in range(3):
		if B[i][0]==B[i][1] and B[i][0]==B[i][2] and B[i][0]!='0':
			return('Player',B[i][0],'wins')
		if B[0][i]==B[1][i] and B[0][i]==B[2][i] and B[0][i]!='0':
			return('Player',B[0][i],'wins')

	if B[0][0]==B[1][1] and B[0][0]==B[2][2] and B[0][0]!='0':
		return('Player',B[0][0],'wins')
	if B[0][2]==B[1][1] and B[0][2]==B[2][0] and B[0][0]!='0':
		return('Player',B[1][1],'wins')
	return('No winner','' ,'' )
	
B=[]

for i in range(3):
	B.append([i for i in input()])
	
(a,b,c) = TicTacToe(B)
if b == '':
	print(a)
else:
	print(a,b,c)
