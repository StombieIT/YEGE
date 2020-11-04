with open('28130_B.txt', 'r') as file:
	nums = (int(n) for n in file.readlines()[1:])
	osts = [[0, 0] for _ in range(81)]
	for num in nums:
		ost = num % 80
		if num <= 50:
			osts[ost][0] += 1
		else:
			osts[ost][1] += 1

c = 0
for i in range(len(osts) // 2 + 1):
	j = -i - 1
	if i == 0 or i == 40:
		c += osts[i][0] * osts[i][1] + osts[i][1] * (osts[i][1] - 1) // 2
	else:
		c += osts[i][1] * (osts[j][0] + osts[j][1]) + osts[j][1] * osts[i][0]
	print(f'{i}\t{osts[i]}\t|\t{len(osts)+j}\t{osts[j]}')

print(c)
