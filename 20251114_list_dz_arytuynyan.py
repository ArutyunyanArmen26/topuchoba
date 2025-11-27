# [На 8 баллов]

#Компьютер в цикле запрашивает у пользователя целые
#числа до тех пор, пока пользователь не введёт 0.

#Полученное от пользователя число заносится компьютером
#или в список чётных чисел (если число чётно), или
#в список нечётных чисел (если число нечётно).

#По окончании цикла компьютер выводит сначала список
#чётных чисел, а затем нечётных.
is_program_work = True
even_numbers = []
odd_numbers = []

while is_program_work:
    num = input("Введите целое число:").strip()
    num = int(num)
    if num == 0:
        is_program_work = False
    if num %2 == 0:
        even_numbers.append(num)
    elif num %2 != 0:
        odd_numbers.append(num)

print(even_numbers)
print(odd_numbers)


#Задание [На 10 баллов]
#Компьютер загадывает длину списка от 0 до 10.
#Далее компьютер наполняет список загаданное число раз
#случайными числами от -100 до 100 и находит максимум
#среди этих чисел.
#Для пустого списка максимум - это None.
#(Не использовать функцию max!)
#Например, компьютер построил список:
#    [4, -67, 6, 95, 95, 11, -34]
#Тогда максимум:
#    95
import random

list_length = random.randint(0, 10)
random_numbers = []
max_value = None

if list_length > 0:
    for _ in range(list_length):
        random_number = random.randint(-100, 100)
        random_numbers.append(random_number)
    max_value = random_numbers[0]
    for number in random_numbers:
        if number > max_value:
            max_value = number
print(random_numbers)
print(max_value)

#Задание [На 12 баллов]

#Компьютер загадывает длину списка от 0 до 10.

#Далее компьютер наполняет список загаданное число раз
#случайными числами от -100 до 100 и находит ПРЕДМАКСИМУМ
#среди этих чисел.

#Предмаксимум - это такое значение, которое может стать
#максимумом, если убрать текущий максимум; то есть
#предмаксимум больше всех значений, кроме максимума.

#Для пустого списка предмаксимум - это None.

#(Можно использовать функцию max!)

#Например, компьютер построил список:
#    [4, -67, 6, 95, 95, 11, -34]

#Тогда предмаксимум:
#    11
import random

list_length2 = random.randint(0, 10)
random_numbers2 = []
predmax_val = None
if list_length2 > 0:
    for _ in range(list_length2):
        random_number2 = random.randint(-100, 100)
        random_numbers2.append(random_number2)
    predmax_val = random_numbers2[0]
    for number2 in random_numbers2:
        if number2 > predmax_val and number2 < max(random_numbers2):
            predmax_val = number2
print(random_numbers2)
print(predmax_val)