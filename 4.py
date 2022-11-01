f = open("24_4.txt")
mn = 1000000000000
B = []
for s in f.readlines():
	count = 1
	if s.count("N") < mn:
		mn = s.count("N")
		B = s
print(B.count('A'),'A')
print(B.count('B'),'B')
print(B.count('C'),'C')
print(B.count('D'),'D')
print(B.count('E'),'E')
print(B.count('F'),'F')
print(B.count('G'),'G')
print(B.count('H'),'H')
print(B.count('I'),'I')
print(B.count('J'),'J')
print(B.count('K'),'K')
print(B.count('L'),'L')
print(B.count('M'),'M')
print(B.count('N'),'N')
print(B.count('O'),'O')
print(B.count('P'),'P')
print(B.count('Q'),'Q')
print(B.count('R'),'R')
print(B.count('S'),'S')
print(B.count('T'),'T')
print(B.count('U'),'U')
print(B.count('V'),'V')
print(B.count('W'),'W')
print(B.count('X'),'X')
print(B.count('Y'),'Y')
print(B.count('Z'),'Z')

