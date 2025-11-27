#Попросить пользователя ввести границы диапазона
chislo1 = input('Введите нижнюю границу диапазона:')
chislo2 = input('Введите верхнюю границу диапазона:')
chislo1 = int(chislo1)
chislo2 = int(chislo2)

#Вывести, не используя параметр "шаг", все числа, которые делятся на 6 в указанном диапазоне
print('1)')
for a in range (chislo1, chislo2 +1):
    if a %6 == 0:
        print(a)
#вывести все двузначные числа с нулем на конце
print('2)')
if chislo2 < 10:
    print('В диапазоне нет двузначных чисел')
else:
    for b in range (10, 100 + 1):
        if b %10 == 0:
            print(b)
#вывести все трехзначные числа, которые делятся на 13
print('3)')
for d in range (100, 1000):
    if d %13 == 0:
        print(d)  
#вывести в обратном порядке все числа меньше тысячи, которые делятся на 13, но не делятся на 14
print('4)')
for c in reversed(range(1, 1000 + 1)):
    if c %13 == 0 and c %14 != 0:
        print(c)
#Напечатать все четные числа от 0 до 1000
print('5)')
for e in range(0, 1000 + 1):
    if e %2 == 0:
        print(e)

#Напечатать все нечетные числа того же диапазона
print('6)')
for f in range(0, 1000 + 1):
    if f %2 != 0:
        print(f)
#Напечатать все числа диапазона, в составе которых есть цифра 3
print('7)')
for g in range(chislo1, chislo2 +1):
    if '3' in str(g):
        print(g)
#Напечатать все трехзначные числа, кончающиеся на 7
print('8)')
for h in range(100, 1000):
    if h %10 == 7:
        print(h)
#Напечатать все двузначные числа с четной суммой цифр
print('9)')
for i in range(10, 100):
    edinizy = i % 10
    desyatky = i // 10
    if (edinizy + desyatky) %2 == 0:
        print(i)
#Напечатать все трехзначные числа без нуля
print('10)')
for j in range(100, 1000):
    if '0' in str(j):
        print
    else:
        print(j)
#Напечатать     0     -1        1       -2      2     -3     3      до     20   -20
print('11)')
print(0)
for k in range (1, 20 + 1):
    print(-k)
    print(k)
#Напечатать    1,     100,     2,     99,     3,     98… до "встречи"
print('12)')
left = 1
right = 100
while left <= right:
    print(left, end=" ")
    if left != right:
        print(right, end=" ")
    left += 1
    right -= 1
print()
#С помощью range вывести все нечётные числа от 77 до 777 включительно
print('13)')
for m in range(77, 777 + 1):
    if m %2 != 0:
        print(m)
#А теперь - используя переменные
#А теперь, получив диапазон от пользователя
#С помощью среза вывести  каждый третий символ любого текста
print('14)')
otvet = 'Привет меня зовут Армен'[::3]
print(otvet)
#С помощью среза и range двумя способами вывести три последних слова текста
print('15)' + 'Первый способ с помощью среза')
text ='Привет меня зовут Армен, а тебя?'
new_text = text.split()
last_three_words = new_text[-3:]
print(last_three_words)

print('16)' + 'Второй способ с помощью range')
new_text = text.split()
last_three_words = [new_text[z] for z in range(max(0, len(new_text) -3), len(new_text))]
print(last_three_words)



colleagues = ['Вася','Ася','Мася']
print('Дорогой,', colleagues[0], '!' )
print('Приходи в пятницу на хэллоуин!')

colleagues = ['Вася','Ася','Мася']
print('Дорогой,', colleagues[1], '!' )
print('Приходи в пятницу на хэллоуин!')

colleagues = ['Вася','Ася','Мася']
print('Дорогой,', colleagues[2], '!' )
print('Приходи в пятницу на хэллоуин!')