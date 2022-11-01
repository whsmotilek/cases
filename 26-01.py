f = open("26-01.txt")
n, k  = map(int, f.readline().split())
A = []
for i in range(n):
	A.append(int(f.readline()))
A.sort()
s = 0
for i in range(k, len(A)-k):
	s += A[i]
	j = A[i]
s = int(s / (n - 2 * k))
print(s,j)