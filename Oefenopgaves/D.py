scrambled = input()
key = input()
keyL = len(key)
text =''
base = ord('a')

for i in range(len(scrambled)):
	g = ord(scrambled[i])-ord(key[i%keyL])
	g = base+g%26
	text+=chr(g)

print(text)

	

	
