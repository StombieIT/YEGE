with open('26-1.txt', 'r') as file:
	S, N = [int(n) for n in next(file).split()]
	P = [int(n) for n in file]

for i in range(len(P)):
	for j in range(N - 1 - i):
		if P[j] > P[j + 1]:
			P[j], P[j + 1] = P[j + 1], P[j]

sm = []

for i in range(len(P)):
	if sum(sm) + P[i] <= S:
		sm.append(P.pop(i))
	else:
		break

for i in range(len(sm)):
	Pimx = P.index(max(P))
	if (
		P[Pimx] + sum(sm) - sm[i] <= S
		and P[Pimx] + sum(sm) - sm[i] > sum(sm)
	):
		sm[i] = P.pop(Pimx)

print(S // max(sm) + 1)
