b = 160
p = 7

with open('28129_B.txt', 'r') as file:
	next(file)
	ostsmx = [0 for _ in range(b)]
	ostsmxp = [0 for _ in range(b)]
	for line in file:
		num = int(line)
		ost = num % b
		if num % p == 0:
			if num > ostsmxp[ost]:
				ostsmxp[ost] = num
		else:
			if num > ostsmx[ost]:
				ostsmx[ost] = num

n1 = n2 = 0

for i in range(len(ostsmx)):
	for j in range(len(ostsmxp)):
		if i != j and ostsmx[i] != 0 and ostsmxp[j] != 0:
			if ostsmx[i] + ostsmxp[j] > n1 + n2:
				n1, n2 = ostsmx[i], ostsmxp[j]

print(n1, n2)
