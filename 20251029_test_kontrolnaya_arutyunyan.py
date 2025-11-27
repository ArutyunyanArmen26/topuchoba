#Дан список

lst = [1, 22, '74', 333, '5', 6, 37, 11]

#1. Вывести числа из списка в столбик. Строки не выводить (вручную, без ветвления)
print('Первое задание')
print()
print(lst[0])
print(lst[1])
print(lst[3])
print(lst[5])
print(lst[6])
print(lst[7])
print()
#2. Сохранить строки из списка в две переменные, приведя к типу int
print('Второе задание')
print()
num_1_str = lst[2]
num_2_str = lst[4]
num_1 = int(num_1_str)
num_2 = int(num_2_str)
print(num_1)
print(num_2)
print()
#3. Вывести числа, которые делятся на 37 (циклом! строки не выводить!)
print('Третье задание')
print()
for i in lst:
    if isinstance(i, int):
        if i % 37 == 0:
            print(i)  
print()           
#4. Решить задачу 3 с помощью исключений
print('Четвертое задание')
print()
for d in lst:
    try:
        if d %37 == 0:
            print(d)
    except TypeError:
        continue