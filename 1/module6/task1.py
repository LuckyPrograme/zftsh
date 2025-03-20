a = input().split('.')
nums = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if a[0] == '2':
    year = int(a[1])
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = 29
    else:
        days = 28
else:
    days = nums[int(a[0]) - 1]
print(f'В этом месяце: {days} дней')
