#Python 3.8.3
#Задание Б
N = int(input())

allnum = {} #Создаём словарь с ключами - значения которые записывает снегурочка, значениями - их количество

for i in range(N):
	m = input()
	D = int(m.split()[0])
	K = int(m.split()[1])
	ost = K % D
	try:
		allnum[ost] += 1
	except KeyError:
		allnum[ost] = 1

mx = 0
num = 0

for key, value in allnum.items():
	if value >= mx and key > num:
		mx = value
		num = key
print(num)
