#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Задача 3
#Пример:
#10 -> 1 2 4 8

n=int(input())
p=1
while p<=n:
    print(p,end=' ')
    p=p*2
