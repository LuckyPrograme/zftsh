num = list(input('Введите число: '))
count = 0
for i in num:
    if int(i) % 2 == 0:
        count += 1
print(f'Количество четных чисел: {count}')
