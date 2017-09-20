a = int(input())
first = a // 1000
last = a % 1000
if first//100 + first%100//10 + first%10 == last//100 + last%100//10 + last%10:
    print('Счастливый')
else:
    print('Обычный')
