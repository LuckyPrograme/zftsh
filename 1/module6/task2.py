n, k = map(int, input('Введите два числа через пробел, для которых надо найти НОД: ').split())

while n != 0 and k != 0:
    if n > k:
        n = n % k
    else:
        k = k % n

print('НОД:', n+k)
