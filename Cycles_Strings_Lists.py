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
    
#Задание 2 - passed
a = [int(i) for i in input().split()]
a2 = [0]*len(a)
if len(a) != 1:
    for i in range(len(a)-1):
        if i <= len(a):
            a2[i] = a[i+1] + a[i-1]
            print(a2[i], end=" ")
    a2[-1] += a[0] + a[-2]
    print(a2[-1])
else:
    print(a[0])
    
# Задание 3 - passed
# вводить цифры пока их сумма не станет 0, затем вывести сумму введенных квадратов
s = int(input())
qu = s**2
while s != 0:
    a = int(input())
    s += a
    qu += a*a
print(qu)

# Задание 4 - passed
#Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку. 
#Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
n = int(input())
s = []
count = 0
b = 1
for i in range(n):
    if count != b:
        print(b, end=" ")
        count += 1
    else:
        count = 1
        b +=1
        print(b, end=" ")
