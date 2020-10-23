with open('24.txt', 'r') as file:
	line = file.read()

c = mx = 0

for i in range(1, len(line)):
	if (
		(line[i-1] == 'L' and line[i] == 'D')  # Если пред. = L и след. = D
		or (line[i-1] == 'D' and line[i] == 'R')  # Если пред. = D и след. = R
		or (line[i-1] == 'R' and line[i] == 'L')  # Если пред. = R и след. = L
	):
		c += 1
	else:
		if c > mx:
			mx = c
		c = 0  #  Обнуляем для нового счёта

print(mx + 1)  # Прибавляем единицу так как алгоритм не считает первую букву последовательности
