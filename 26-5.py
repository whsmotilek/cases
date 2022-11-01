f = open("26-5.txt")
n = int(f.readline())
A = []
s = 0 
for i in range(n):
	k = int(f.readline())
	A.append(k)
	s += k

s = s * 0.6 #всего нужно внести
b = 
r = s - b #взнос всех остальных 
print(A,s)