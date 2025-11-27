#[8 баллов]
#1. Задвоить элементы в списке. То есть компьютер превращает
#список [4, print, "xyz", None] в список [4, 4, print, print,
#"xyz", "xyz", None, None]

#(Варианты решений этой задачи в файлах "ex6.py" и "ex6_v2.py".)

list = [4, print, "xyz", None]
double_list = []

for index, item in enumerate(list[:]):
    list.insert(index * 2, item)
print(list)
print()



#[10 баллов]
#2. Компьютер спрашивает у пользователя, сколько тот хочет
#положить в список целых чисел.

list_numbers = []

numders = input("Сколько целых чисел вы хотите положить в список(ответ цифровым значением): ").strip()
numders = int(numders)
print()


#Далее указанное число раз компьютер запрашивает у пользователя
#эти числа.

for i in range(numders):
    number = input("Введите число № %i:" % (i + 1))
    list_numbers.append(number)
print()


#Потом компьютер выводит построчно элементы списка, указывая
#их индекс.

index = 0

for index, number in enumerate(list_numbers):
     print(index, "-", number, end = ", ")
     index += 1
print()


#Затем удаляет из списка те числа, что находятся в нём под нечётными
#индексами (счёт с нуля).
#Потом компьютер опять выводит построчно элементы списка, указывая
#их индекс.

index_remove = []

for index in range(len(list_numbers)):
    if index %2 != 0:
        index_remove.append(index)
for index in reversed(index_remove):
    del list_numbers[index]
for index, number in enumerate(list_numbers):
    print(index, "-", number, end = ",")
print()


#[10 баллов]
#3. Компьютер загадывает длину списка от 0 до 10. Далее компьютер
#наполняет список загаданное число раз случайными числами от -100
#до 100 и находит максимум среди этих чисел.
#(Не использовать функцию max!)
import random
chisla = []

length_list = input("Введите длину списка (от  0 до 10):").strip()
length_list = int(length_list)

for t in range(random(-100, 100)) :
        chisla.append(t)
print(chisla)




#[11 баллов]
#4. Компьютер запрашивает количество сотрудников, и далее указанное
#число раз запрашивает у пользователя имя и фамилию сотрудника в виде
#одной строки (то есть имя и фамилия вводятся через пробел), компьютер
#заносит фамилию в один список, имя - в другой. Потом выводит
#имена и фамилии построчно так: на каждой строке имя-пробел-фамилия.