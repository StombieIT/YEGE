# Решу ЕГЭ задание 27 № 15964
# Python 3
N = int(input()) # Кол-во элементов
mx52 = mx5 = mx2 = mx = 0
for i in range(N):
	c = int(input()) # Элемент
	if c % 5 == 0 and c % 2 == 0 and c > mx52: # Если кратно 5 и 2 и больше максимального данного элемента
		mx52 = c
	elif c % 5 == 0 and c > mx5: # Если больше и кратно 5
		mx5 = c
	elif c % 2 == 0 and c > mx2: # Если больше и кратно 2
		mx2 = c
	elif c > mx: # Если больше
		mx = c
if mx52 * mx > mx5 * mx2:
	print(mx52, mx)
else:
	print(mx5, mx2)
