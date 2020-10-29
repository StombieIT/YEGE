with open('28133_A.txt', 'r') as file:
	next(file)
	ostd120 = [0 for _ in range(121)]
	for line in file:
		num = int(line)
		ost = num % 120
		if num > ostd120[ost]:
			ostd120[ost] = num

n1 = n2 = mxs = 0

for i in range(len(ostd120) // 2):
	if ostd120[i] != 0 and ostd120[-(i + 1)] != 0 and ostd120[i] + ostd120[-(i + 1)] > mxs:
		mxs = ostd120[i] + ostd120[-(i + 1)]
		n1, n2 = ostd120[i], ostd120[-(i + 1)]

print(n1, n2)
print(mxs)
print(f'{mxs} % 120 = {mxs%120}')