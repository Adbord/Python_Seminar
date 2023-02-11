# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


n = int(input('Введите количество элементов в set1: '))
m = int(input('Введите количество элементов в set2: '))

set1 = set()
set2 = set()

print('Введите элементы в set1:')
for i in range(n):
    element = int(input())
    set1.add(element)

print('Введите элементы в set2:')
for i in range(m):
    element = int(input())
    set2.add(element)

intersection_set = set1 & set2

sorted_intersection_set = sorted(intersection_set)

print('Числа, встречающиеся в обоих наборах без повторения и в порядке возрастания:')
for element in sorted_intersection_set:
    print(element)

