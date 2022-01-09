# урок 1 задача 2

# список нечётных чисел в кубе
list_odd_cube = []

# общая сумма чисел, сумма которых делится на 7
sum = 0

for i in range(1000):
    if not (i % 2 == 0):
        list_odd_cube.append(i**3)
#    if i == 30:
#        break

for el in list_odd_cube:
    print(el)

for num in list_odd_cube:
    sum_num = 0
    num += 17
    while num % 10 != 0:
        sum_num += num % 10
        num = num // 10

    print(sum_num)

    if sum_num % 7 == 0:
        sum += sum_num

print('sum =', sum)