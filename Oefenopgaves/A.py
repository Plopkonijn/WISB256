lines = int(input())
line = ''
for i in range(lines):
	line = input()
	if len(line.split())<=4:
		print(line,'krAh!')
	else:
		print('Crackers!')