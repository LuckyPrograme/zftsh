count = 0
for i in range(10**6, 10**7):
    first = 1
    second = 1
    n = i
    while n > 10:
        last = n % 10
        if len(str(n)) >= 4:
            second *= last
        else:
            first *= last
        n //= 10
    if first == second:
        count += 1
print(count)
