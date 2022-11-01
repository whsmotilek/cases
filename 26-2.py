f = open("26-2.txt")
n, k = map(int,f.readline().split())
A = [0] * n #вес
B = [0] * n  #стоимость
for i in range(n):
	A[i], B[i] = map(int,f.readline().split())
C = [0] * n
for i in range(n):
	C[i] = B[i] / A[i]

for i in range(n-1):
	for j in range(i+1, n):
		if C[i] > C[j]:
			C[i], C[j] = C[j], C[i]
			A[i], A[j] = A[j], A[i]
			B[i], B[j] = B[j], B[i]
m3 = -1 #максимальный индекс при котором С равно 9.0 
l = -1
for i in range(n):
	if (C[i] == C[k]) and (l == -1):
		l = i
	if (C[i] == C[k]) and (i > m3):
		m3 = i

for i in range(l, m3 - 1):
	for j in range(i+1, m3):
		if A[i] < A[j]:
			A[i], A[j] = A[j], A[i]
			B[i], B[j] = B[j], B[i]
#32
#53
j = 0
m2 = 0 
l = 0 
for i in range(k):
	j += A[i]
	if A[i] > m2:
		m2 = A[i]
		l = B[i]

print(j,l)