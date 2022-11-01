print("Задание 19")
def F(x, p):
	if  (x >= 70) and (p == 2):
		return True
	else:
		if (x < 70) and (p == 2):
			return False
		else:
			if (x >= 70):
				return False
	if p % 2 == 1:
		return F(x + 1,p + 1) or F(x * 3 - 1,p + 1)
	else:
		return F(x + 1,p + 1) and F(x * 3 - 1,p + 1)

for x in range(1,100):
	if F(x, 1):
		print(x)
		break
print("Задание 20")
def F(x, p):
	if  (x >= 70) and (p == 4):
		return True
	else:
		if (x < 70) and (p == 4):
			return False
		else:
			if (x >= 70):
				return False
	if p % 2 == 1:
		return F(x + 1,p + 1) or F(x * 3 - 1,p + 1)
	else:
		return F(x + 1,p + 1) and F(x * 3 - 1,p + 1)
for x in range(1,100):
	if F(x, 1):
		print(x)
print("Задание 21")
def F(x, p):
	if  (x >= 70) and ((p == 3) or (p == 5)):
		return True
	else:
		if (x < 70) and (p == 5):
			return False
		else:
			if (x >= 70):
				return False
	if p % 2 == 0:
		return F(x + 1,p + 1) or F(x * 3 - 1,p + 1)
	else:
		return F(x + 1,p + 1) and F(x * 3 - 1,p + 1)
def f(x, p):
	if  (x >= 70) and (p == 3):
		return True
	else:
		if (x < 70) and (p == 3):
			return False
		else:
			if (x >= 70):
				return False
	if p % 2 == 0:
		return f(x + 1,p + 1) or f(x * 3 - 1,p + 1)
	else:
		return f(x + 1,p + 1) and f(x * 3 - 1,p + 1)
for x in range(100,0,-1):
	if F(x, 1):
		print(x)
		
for x in range(100,0,-1):
	if f(x, 1):
		print(x, 'лишнее')
		