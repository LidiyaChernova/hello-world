#Задание 1

#Дано: aaaabbcccd
#Надо: a4b2c3d1

string = aaaabbcccd
i = 0
j = 1
count = 0
for i in string:
	for j in string:
		if i == j:
			count += 1
			i += 1
			j += 1
		elif:
			count += 1
			print(i, end="")
			print(count, end="")
			i += 1
			j += 1
			count = 0
continue
		else:
			count += 1
			print(i, end="")
			print(count)
