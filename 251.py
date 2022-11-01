count = 0
s = 0

for x in range(1024, 289213):
	k = True
	for n in range(2, int(x ** 1/2) + 1):
		if x % n == 0:
			k == False
			break
	if k:
		s += x
print(s)