with open('27991_B.txt', 'r') as file:
	next(file)
	mx17 = mxn = 0
	for line in file:
		num = int(line)
		if num > mx17 and num % 17 == 0:
			mx17 = num
		elif num > mxn and (num - mx17) % 2 == 0:
			mxn = num

print(mx17, mxn)
