# Решу ЕГЭ задание 27 № 15812
# Python 3
N = int(input()) #Кол-во элементов
x = 0 # Не делится ни на 2, ни на 3
x2 = 0 # Делится на 2, но не делится на 3
x31 = 0 # Делится на 3, но не делится на 2
x32 = 0 # Делится и на 2, и на 3
for i in range(N):
	c = int(input()) # Получаем элемент
	if c % 3 == 0: # Если делится на 3
		if c % 2 == 0: # Если делится на 2
			x32 += 1
		else: # Если не делится на 2
			x31 += 1
	elif c % 2 == 0: # Если не делится на 3, но делится на 2
		x2 += 1
	else: # Если не делится ни на 3, ни на 2
		x += 1
print(x31 * x2 + x31 * x32 + x32 * x)