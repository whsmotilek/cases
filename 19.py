print("Задача 19")
def F(x, p):
	if x >= 39 and p == 2:
		return True
	else:
		if x < 39 and p == 2:
			return False
	return F(x + 1,p + 1) or F(x * 3 ,p + 1) 
for i in range(1, 100):
	if F(i, 1):
		print(i)
		break
print("Задача 20")
def F(x, p):
	if x >= 39 and p == 4:
		return True
	else:
		if x < 39 and p == 4:
			return False
		else:
			if x >= 39:
				return False
	if p % 2 == 1:
		return F(x + 1,p + 1) or F(x * 3 ,p + 1) 
	else:
		return F(x + 1,p + 1) and F(x * 3 ,p + 1) 
for i in range(1, 100):
	if F(i, 1):
		print(i)
print("Задача 21")
def F(x, p):
	if x >= 39 and p == 5:
		return True
	else:
		if x < 39 and p == 5:
			return False
		else:
			if x >= 39:
				return False
	if p % 2 == 0:
		return F(x + 1,p + 1) or F(x * 3 ,p + 1) 
	else:
		return F(x + 1,p + 1) and F(x * 3 ,p + 1) 
for i in range(1, 100):
	if F(i, 1):
		print(i)

#44
#33 42
#41