def b(l):  # Сортировка пузырьком
	for i in range(len(l)):
		for j in range(len(l) - i - 1):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
	return l

with open('26_28140.txt', 'r') as file:
	S, N = [int(n) for n in next(file).split()]
	m = b([int(n) for n in file])  # Получаем сразу отсортированный список чисел

mx = []  # Список из максимального кол-ва пользователей

while True: 
	# Составляем данный список, но из списка m его элементы удаляются
	la = m.pop(m.index(min(m)))
	if sum(mx) + la <= S:
		mx.append(la)
	else:
		break

while True: 
	'''
	Меняем максимальные значения списка mx на минимальные значения списка m,
	дабы достигнуть максимальной возможной суммы mx, не утрачивая максимального
	количества пользователей => найдём максимальный возможный элемент
	'''
	la = m.pop(m.index(min(m)))
	if sum(mx) - max(mx) + la <= S:
		del mx[mx.index(max(mx))]
		mx.append(la)
	else:
		break

print(len(mx), max(mx))
