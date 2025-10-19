#найти дату рождения, сегодня 7.10.2025 год
year = 2025
month = 10
day = 7
a = input('Введите год рождения:')
b = input('Введите месяц рождения в числовом значении:')
c = input('Введите день рождения:')
a = int(a)
b = int(b)
c = int(c)
age = year-a
if month<b or(month==b and day<c):
    age = age-1

print('Вам',+age,'лет')
