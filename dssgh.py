weather = input('Какая погода?')
t = input('А сколько градусов?')
t =int(t)
decision = ''
if weather == 'sun':
    if t < 10:
        decision = 'оденемся потеплее и '
    decision += 'пойдём гулять'
if weather == 'rain':
    decision = 'Возьмём зонтик'
    if t < 0:
        decision = 'Наденем кроссовки с шипами'
print(decision)