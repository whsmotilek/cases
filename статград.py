f = open('26-06.txt')
n, m = map(int, f.readline().split())
A = [0] * n
B = [0] * n
C = [0] * n
A1 = []
B1 = []
A2 = []
B2 = []
for i in range(n):
	A[i], B[i], C[i] = f.readline().split()
	A[i] = int(A[i])
	B[i] = int(B[i])
s = m
for i in range(n):
	if C[i] == 'A':
		A1.append(A[i])
		B1.append(B[i])
	else:
		A2.append(A[i])
		B2.append(B[i])
for i in range(len(A1) - 1):
	for j in range(i + 1, len(A1)):
		if A1[i] > A1[j]:
			A1[i], A1[j] = A1[j], A1[i]
			B1[i], B1[j] = B1[j], B1[i]
for i in range(len(A2) - 1):
	for j in range(i + 1, len(A2)):
		if A2[i] > A2[j]:
			A2[i], A2[j] = A2[j], A2[i]
			B2[i], B2[j] = B2[j], B2[i]
g = 0
for i in range(len(A2)):
	for j in range(B2[i]):
		if s - A2[i] >= 0:
			s = s - A2[i]
for i in range(len(A1)):
	for j in range(B1[i]):
		if s - A1[i] >= 0:
			s = s - A1[i]
			g += 1
print(g,s)