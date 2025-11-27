#Задача [на 10 баллов]

#Компьютер спрашивает, сколько целых чисел надо
#положить в список. Затем запрашивает сами числа
#указанное число раз. (Если количество чисел
#задаётся пользователем как отрицательное или ноль,
#то создаётся пустой список.)
list_numbers = []

number = input('Ведите сколько целых чисел надо положить в список:').strip()
number = int(number)

for i in range(number):
    numbers = input('Введите число # %i:' % (i + 1)).strip()
    numbers = int(numbers)

    if number > 0:
        list_numbers.append(numbers)
        
    else:
        None
print(f"{list_numbers = }")

#На основе полученного списка компьютер создаёт
#новый список, в котором все чётные значения из
#первого списка заменены на 8, а нечётные на -1.
new_list_numbers = []

for numbers_2 in list_numbers:
    if numbers_2 %2 == 0:
        numbers_2 = 8
        new_list_numbers.append(numbers_2)
    elif numbers_2 %2 != 0:
        numbers_2 = -1
        new_list_numbers.append(numbers_2)
print(f"{new_list_numbers = }")

#То есть, например, для введённого списка
#    [5, -6, -10, -7, 3]
#будет создан список
#    [-1, 8, 8, -1, -1]