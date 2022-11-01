f = open("24_2.txt")
n = f.readline()
count = 1
mx = 0
for i in range(len(n)):
	if n[i] == 'A':
		count += 1
	else:
		if count > mx:
			mx = count
		count = 0
print(mx)