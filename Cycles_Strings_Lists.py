#Задание 1

#Дано: aaaabbcccd
#Надо: a4b2c3d1

d = "aaabbcccf"
j = 1

for i in range (1, len(d)):
    if d[i] == d[i - 1]:
        j+=1
    else:
        print(d[i - 1], end = "")
        print(j, end = ""),
        j = 1

print(d[i], end = ""),
print(j)
