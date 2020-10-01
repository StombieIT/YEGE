with open('24-1.txt', 'r') as file:
	line = file.readline()

count = 1

for sym in line:
	if sym == '1':
		count += 1
	elif sym == '4':
		count *= 4
	elif sym == '7':
		count %= 7

print(count)
