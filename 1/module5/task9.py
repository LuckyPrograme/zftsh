import random

massiv = random.choices(range(2, 255, 2), k=25)
print('Массив:', massiv, '\nСумма его элементов:', sum(massiv))
