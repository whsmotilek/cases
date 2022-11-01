f = open("24_5.txt")
n = f.readline()
count = 0
mx = 0
for i in range(1,len(n)-1):
	if n[i-1] != n[i+1]:
		count += 1
	else:
		if count > mx:
			mx = count
		count = 0
print(mx)