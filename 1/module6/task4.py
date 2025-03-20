import random

random_values = random.choices(range(1, 144), k=12)
print(f'Случайные значения: {random_values}\nОтсортированные: {sorted(random_values)}')
