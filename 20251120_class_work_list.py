#В этих задачах таблицей будет назваться структура данных
#список списков, то есть вот, например такое:
#    [[3, 4], [6, 7], [-1, 2], [-8, 0]]
#Что можно распечатать как:
#    3   4
#    6   7
#    -1  2
#    -8  0



#Задача 1

#Распечатка элементов таблицы, основанной на списках в списке:
#    не так:
#        [[1, 2, 6, 4], [0, 5, 5, 1], [7, 7, 8, 6]]

#    не так:
#        [1, 2, 6, 4]
#        [0, 5, 5, 1]
#        [7, 7, 8, 6]

#    а так:
#        1   2   6   4
#        0   5   5   1
#        7   7   8   6
print("Вариант 1:")
print()

list_number = [[1, 2, 6, 4], [0, 5, 5, 1], [7, 7, 8, 6]]

a = list_number[0]
b = list_number[1]
c = list_number[2]

print(a[0], a[1], a[2], a[3])
print(b[0], b[1], b[2], b[3])
print(c[0], c[1], c[2], c[3])
print()

print("Вариант 2:")
print()

list_number = [[1, 2, 6, 4], [0, 5, 5, 1], [7, 7, 8, 6]]

for i in list_number[0]:
    print(i, end = " ")
print()
for d in list_number[1]:
    print(d, end = " ")
print()
for b in list_number[2]:
    print(b, end = " ")
print()
    
list_number = [[1, 2, 6, 4], [0, 5, 5, 1], [7, 7, 8, 6]]

for n in range(len(list_number)):
    for u in range(len(list_number[n])):
        print(list_number[n][u], end = " ")
    print()


