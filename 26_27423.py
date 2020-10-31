with open('26_27423.txt', 'r') as file:
	S, N = [int(n) for n in next(file).split()]
	a = [int(n) for n in file]
a.sort()

p = []

while True:
	mna = min(a)
	if sum(p) + mna <= S:
		p.append(mna)
		del a[a.index(mna)]
	else:
		break

while True:
	mna = min(a)
	mxp = max(p)
	smp = sum(p)
	if smp <= smp - mxp + mna <= S:
		del p[p.index(mxp)]
		p.append(mna)
		del a[a.index(mna)]
	else:
		break

print(p)
print(len(p), max(p))