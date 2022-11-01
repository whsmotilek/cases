f = open('27-B.txt')
n = int(f.readline())
A = []
k = 5
for i in range(k):
	A.append(int(f.readline()))

#print(A)
n29 = 0
count = 0
for i in range(k, n):
	
	if A[i % k] % 29 == 0:
		n29 += 1
	
	s = int(f.readline())
	if s % 29 == 0:
		count += i - (k-1)
	else:
		count += n29
	print(A, "индекс", i%k, 'проверяемое число', A[i % k],"количество чисел, дел на 29",n29, count)
	A[i % k] = s
	#print(A)
	#print(k % )
print(count)