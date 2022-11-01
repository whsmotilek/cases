print("Задание №19")
def f(x, y, p):
	if (x + y >= 79) and p == 3:
		return True
	else:
		if (x + y < 79) and p == 3:
			return False
	return f(x + 3, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 3, p + 1) or f(x, y*2, p + 1)
for i in range(1,70):
	if f(9,i,1):
		print(i)
		break
print("Задание №20")
def f(x, y, p):
	if (x + y >= 79) and p == 4:
		return True
	else:
		if (x + y < 79) and p == 4:
			return False
		else:
			if x + y >= 79:
				return False
	if p % 2 == 1:
		return f(x + 3, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 3, p + 1) or f(x, y*2, p + 1)
	else:
		return f(x + 3, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 3, p + 1) and f(x, y*2, p + 1)
for i in range(1,70):
	if f(9,i,1):
		print(i)
		break
print("Задание №21")
def f(x, y, p):
	if (x + y >= 79) and ((p == 3) or (p == 5)):
		return True
	else:
		if (x + y < 79) and p == 5:
			return False
		else:
			if x + y >= 79:
				return False
	if p % 2 == 0:
		return f(x + 3, y, p + 1) or f(x * 2, y, p + 1) or f(x, y + 3, p + 1) or f(x, y*2, p + 1)
	else:
		return f(x + 3, y, p + 1) and f(x * 2, y, p + 1) and f(x, y + 3, p + 1) and f(x, y*2, p + 1)
for i in range(1,70):
	if f(9,i,1):
		print(i)
def F(x, y, p):
	if (x + y >= 79) and (p == 3):
		return True
	else:
		if (x + y < 79) and p == 3:
			return False
		else:
			if x + y >= 79:
				return False
	if p % 2 == 0:
		return F(x + 3, y, p + 1) or F(x * 2, y, p + 1) or F(x, y + 3, p + 1) or F(x, y*2, p + 1)
	else:
		return F(x + 3, y, p + 1) and F(x * 2, y, p + 1) and F(x, y + 3, p + 1) and F(x, y*2, p + 1)
for i in range(1,70):
	if F(9,i,1):
		print(i, '----')
		