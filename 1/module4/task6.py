l = list(input("Введите число: "))
n = []

for i in range(len(l)):
    if int(l[i]) % 2 == 1:
        n += l[i]
        l[i] = '*'
count = 0
for j in range(len(l)):
    if l[j] == '*':
        count += -1
        l[j] = n[count]

print(*l, sep='')
