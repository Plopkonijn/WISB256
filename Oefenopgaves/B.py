def operator(x,y,p):
	x = int(x)
	y = int(y)
	if p == '*':
		return x*y
	if p == '/':
		return x/y
	if p == '-':
		return x-y
	if p == '+':
		return x+y

line = input().split()
result = operator(line[0],line[1],line[2])
result = "{0:.3f}".format(result)
print(result)