f = open("26-04.txt")
n , k = map(int, f.readline().split())
A = []
for i in range(n):
	A.append(int(f.readline()))
A.sort()
c = 0
j = 0
for i in range(n-k,len(A)):
	j += A[i] * 0.2
	A[i] = A[i] * 0.8
	c += 1
print(A[n-k-1], int(j))