import math

def are_points_on_circle(points):
    # Берем первые три точки
    (x1, y1), (x2, y2), (x3, y3) = points[:3]
    # Находим центр и радиус окружности, проходящей через первые три точки
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    E = A * (x1 + x2) + B * (y1 + y2)
    F = C * (x1 + x3) + D * (y1 + y3)
    G = 2 * (A * (y3 - y1) - B * (x3 - x1))
    if G == 0:
        return 'Не могут'  # Точки коллинеарны, окружность не существует
    a = (D * E - B * F) / G
    b = (A * F - C * E) / G
    r = math.sqrt((x1 - a)**2 + (y1 - b)**2)
    # Проверяем, лежат ли остальные точки на этой окружности
    for (x, y) in points[3:]:
        if not math.isclose((x - a)**2 + (y - b)**2, r**2, rel_tol=1e-9):
            return 'Не могут'
    return 'Могут'

s = ''
nums = []
count = 1
while s != '0 0':
    s = input(f'Введите координаты точки {count} через пробел: ')
    count = count + 1
    try:
        xy = s.split()
        nums.append([int(xy[0]), int(xy[1])])
    except Exception as e:
        print(e)
        s = '0 0'
        nums.append([0, 0])
nums = nums[:-1]
print(nums)
if len(nums) in [1, 2]:
    print('Могут')
elif len(nums) == 3:
    if nums[0][0] == nums[1][0] == nums[2][0] or nums[0][1] == nums[1][1] == nums[2][1]: # все три точки на лежат на одной прямой
        print('Не могут')
    else:
        print('Могут')
else:
    print(are_points_on_circle(nums))
