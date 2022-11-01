
k = 2
A = [False] * 1001
while k * k <= 10:
	if A[k] == False:
		i = k * k 
		while i <= 1000:
			A[i] = True
			i += k
		k += 1
	else:
		k += 1
B = []
for i in range(2, len(A)):
	if A[i] == False:
		B.append(i)
print(B)
for i in range(len(B)-1):
	for j in range(i+1,len(B)):
		if (B[i] * B[j] >= 95101) and (B[i] * B[j] <= 95130):
			print(B[i]*B[j]*2, B[i] *B[j])
