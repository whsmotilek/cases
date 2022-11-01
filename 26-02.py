f = open("26-02.txt")
n = int(f.readline())
k = int(0.2 * n)
m = int(0.5 * k)
A = []
for i in range(n):
	A.append(int(f.readline()))
A.sort()
s = 0
for i in range(m, len(A) - m):
	s += A[i]
	j = A[i]
print(s,j)