import numpy as np

print('Уравнение: x⁴+bx³+cx²+dx+f=0, f≠=0.\nВведите 4 целых числа - коэффициенты уравнения через пробел')
kefs = list(map(int, input().split()))

print(np.roots([1] + kefs))
