l = list(input())
unic = []
for i in l:
    if i not in unic:
        unic.append(i)
if '0' in unic:
    print((len(unic) - 1) * ((len(unic))**(len(l)-1)))
else:
    print(len(unic) ** len(l))
# количество чисел с учётом введеного числа
