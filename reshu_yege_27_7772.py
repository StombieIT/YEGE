# Решу ЕГЭ задание 27 № 7772
# Python 3.8.3
# Программа является решением задачи А
a = [int(input()) for i in range(int(input()))]
mx = 0
for i in range(len(a)):
	for j in range(i + 8, len(a)):
		if a[j] * a[i] > mx:
			mx = a[j] * a[i]
print(mx)
# Решу ЕГЭ задание 27 № 7772
# Python 3.8.3
# Программа является решением задачи Б
N = int(input())
a = []
for i in range(N):
	a.append(int(input()))
mx1 = -1
posmx1 = -1
mx2 = -1
for i in range(N):
	if a[i] > mx1 and N - 1 - i >= 8: # N - 1 - Позиция последнего символа
		mx1 = a[i]
		posmx1 = i
		continue
	elif a[i] > mx2 and i - posmx1 >= 8:
		mx2 = a[i]
print(mx1 * mx2)
