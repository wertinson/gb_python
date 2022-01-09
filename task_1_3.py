# урок 1 задача 3

for i in range(100):
    num = i + 1
    if num % 10 == 1:
        ending = ''
    elif num % 10 == 2:
        ending = 'а'
    elif num % 10 == 3:
        ending = 'а'
    elif num % 10 == 4:
        ending = 'а'
    else:
        ending = 'ов'

    # исключения
    if num == 11:
        ending = 'ов'
    elif num == 12:
        ending = 'ов'
    elif num == 13:
        ending = 'ов'
    elif num == 14:
        ending = 'ов'

    print(str(num) + ' процент' + ending)