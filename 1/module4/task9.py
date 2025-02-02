import math

def lcm(a, b):
    """Вычисляет НОК двух чисел."""
    return abs(a * b) // math.gcd(a, b)

def lcm_of_sequence(numbers):
    """Вычисляет НОК для последовательности чисел."""
    if not numbers:
        return 0
    current_lcm = numbers[0]
    for number in numbers[1:]:
        current_lcm = lcm(current_lcm, number)
    return current_lcm

# Ввод последовательности чисел
numbers = []
while True:
    num = int(input("Введите натуральное число (0 для завершения): "))
    if num == 0:
        break
    numbers.append(num)

# Вычисление НОК
if numbers:
    result = lcm_of_sequence(numbers)
    print(f"Наименьшее общее кратное: {result}")
else:
    print("Последовательность пуста.")
