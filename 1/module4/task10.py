def max_sum_of_squares_of_roots():
    # Ввод последовательности чисел
    numbers = []
    while True:
        num = int(input("Введите число (1001 для завершения): "))
        if num == 1001:
            break
        numbers.append(num)

    max_sum = -float('inf')  # Начальное значение для поиска максимума

    # Перебор всех пар (b, c)
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue  # Пропускаем пары, где b и c — одно и то же число
            b = numbers[i]
            c = numbers[j]

            # Проверка существования корней (дискриминант >= 0)
            discriminant = b**2 - 4 * c
            if discriminant >= 0:
                # Сумма квадратов корней
                sum_of_squares = b**2 - 2 * c
                if sum_of_squares > max_sum:
                    max_sum = sum_of_squares

    # Вывод результата
    if max_sum != -float('inf'):
        print(f"Максимальная сумма квадратов корней: {max_sum}")
    else:
        print("Нет подходящих пар (b, c).")

# Запуск функции
max_sum_of_squares_of_roots()
