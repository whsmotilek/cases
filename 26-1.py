f = open("26-1.txt")
n = int(f.readline())
A = []
for i in range(n):
	A.append(int(f.readline()))
A.sort()
k = 0
f = True

for i in range(len(A)):
	for j in range(len(A)-1, i, -1):
		if A[i] + A[j] == 100:
			k += 1
			A[i] = 0
			A[j] = 0

print(k)
#3845 - пар 
#8321 - длина массива
# len(A)-1, i