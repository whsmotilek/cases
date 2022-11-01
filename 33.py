f = open("24_3.txt")
n = f.readline()
count = 0
mx = 0
for i in range(1,len(n)):
	if n[i] == "D":
		count += 1
	else:
		if count > mx:
			mx = count
		count = 0
print(mx)
