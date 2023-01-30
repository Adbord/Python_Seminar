# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Задача 4
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no


# n, m, k = int(input()), int(input()), int(input())
# if n*m>k:
#   if k%n == 0 or k%m == 0:
#     print('Yes')
# else:
#       print('No')
# else:
#       print('No')

n = int(input())
m = int(input())
k = int(input())

if k < m*n and (k%m==0 or k%n==0):
  print('Yes')
else:
  print('No')

