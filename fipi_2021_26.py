with open('26.txt', 'r') as file:
	lines = file.readlines()
	S, N = [int(val) for val in lines[0].split()]
	b = []
	b.extend([int(line) for line in lines[1:]])

pz = []
for i in range(N):
	if not sum(pz) + min(b) > S:
		pz.append(
			b.pop(
				b.index(
					min(b)
				)
			)
		)
	else:
		break

for _ in range(len(b)):
	if sum(pz) - max(pz) < sum(pz) - max(pz) + min(b) and sum(pz) - max(pz) + min(b) < S:
		pz[pz.index(max(pz))] = b.pop(
			b.index(
				min(b)
			)
		)

print(len(pz), max(pz))
