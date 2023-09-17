list = [35, 12, -3, 76, 67, -34, 7, 2, 9]
reslist = []
print("Список содержит " + str(list))
# a.sort()
negative = 0
pair = 0
nonpair = 0
multiplication = 1
for i in list:
    if i < 0:
        negative += i
        reslist.append(negative)
print("Створити список цілих, що містить лише негативні числа з першого списку; " + str(reslist))
reslist.clear()
for z in list:
    if z % 2 == 0:
        reslist.append(z)
        pair += z
print("Створити список цілих, що містить лише парні числа з першого списку; " + str(reslist))
reslist.clear()
for y in list:
    if y % 2 != 0:
        nonpair += y
        reslist.append(y)
print("Створити список цілих, що містить лише непарні числа з першого списку; " + str(reslist))
reslist.clear()
for x in list:
    if x % 3 == 0:
        if x > 0:
            multiplication *= x

for u in list:
    if u > 0:
        reslist.append(u)
        minmax = min(reslist) * max(reslist)
print("Створити список цілих, що містить лише позитивні числа з першого списку." + str(reslist))
print("Добуток елементів між мінімальним та максимальним елементом; " + str(minmax))
print("Добуток елементів з кратними індексами 3; " + str(multiplication))
print("Суму парних чисел; " + str(nonpair))
print("Суму непарних чисел; " + str(pair))
print("Суму негативних чисел; " + str(negative))
