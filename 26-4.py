f = open("26-4.txt")
n, k, m = map(int,f.readline().split())
A = []
for i in range(n):
	A.append(int(f.readline()))
B = [] #бюджет
A.sort()
for i in range(k):
	B.append(A[i])
s = 0
for i in range(len(B)):
	s += B[i]
r = int(s / len(B))
print(A[n-m], r)