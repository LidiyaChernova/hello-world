#Задание 1

#Дано: aaaabbcccd
#Надо: a4b2c3d1

d = input()
count = 1
if len(d) == 1:
    print(d[0], end="1")
else:
    for i in range (1, len(d)):
        if d[i] == d[i - 1]:
            count += 1
        else:
            print(d[i - 1], end = "")
            print(count, end = ""),
            count = 1
    print(d[i], end = ""),
    print(count)
