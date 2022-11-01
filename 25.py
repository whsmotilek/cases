# решето Эратосфена
m = 1024
n = 28921277 + 1
A = [False] * n

k = 2
while k * k < n:
	if A[k] == False:
		i = 2 * k
		while i < n:
			A[i] = True
			i += k
	k += 1
s = 0
for i in range(m, n):
	if A[i] == False:
		s += i
print(s)