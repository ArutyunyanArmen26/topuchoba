hour=60
week=300
month=1000
year=20000
data= input('Введите год рождения:')
tariff= input('Введите тариф(час, неделя, месяц, год)')
data=int(data)
age=2025-data
coeff= 1
if age<=14 or age>=50:
    print('Бесплатно')
    coeff = 0
elif age>14 and age<24:
    print('Студент')
    coeff = 0.5
else:
    print('Взрослый')
if tariff == 'час':
    print('Цена проезда', hour * coeff, 'руб')
elif tariff == 'неделя':
    print('Цена проезда', week * coeff, 'руб')
elif tariff == 'месяц':
    print('Цена проезда', month * coeff, 'руб')
elif tariff == 'год':
    print('Цена проезда', year * coeff, 'руб')




