f = open("26-03.txt")
n = int(f.readline())
A = []
s = 0
for i in range(n):
	k = int(f.readline())
	A.append(k)
	s += k
m = 0.9 * s
A.sort()
print(A)
for i in range(len(A)-1, -1, -1):
	A[i] = A[i] * 0.8
	m = m - A[i]
k = 0

for i in range(len(A)):
	q = m
	q = q - A[i] / 4
	if q >= 0: 
		A[i] = A[i] / 0.8
		m = m - A[i] * 0.2 
		k = i
		j = A[i]
mn = m

print(mn)
for i in range(k, -1, -1):
	for g in range(k + 1, len(A)):
		A[i] = A[i] * 0.8
		A[g] = A[g] / 0.8
		j = A[g]
		m = m - A[g] * 0.2 + A[i] * 0.2
		if m >= 0 and m <= mn:
			mn = m
			l = A[i]
		else:
			A[i] =  A[i] / 0.8
			A[g] = A[g] * 0.8

print(l)