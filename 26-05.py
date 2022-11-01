f = open("26-05.txt")
n , k = map(int, f.readline().split())
A = []
for i in range(n):
	A.append(int(f.readline()))
A.sort()
s4 = 0
c = 0 
for i in range(n - 2 * k, n - k):
	s4 += A[i]
s4 = int(s4 / k)
s5 = 0
for i in range(n - k, len(A)):
	s5 += A[i]
	c += 1
s5 = int(s5 / k)
print(s5,s4)