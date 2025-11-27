my_text = '''Я понял, 
как работает    \t\t сплит!'''
print(my_text.split())
['Я', 'понял,', 'как', 'работает', 'сплит!']
split_with_space = my_text.split(' ')
print('Параметр - пробел: ', split_with_space)
print(split_with_space[2])


wxh = input('Введите размер WxH :')
print('wxh: ', wxh)
print('Сплитим по х: ', wxh.split(' '))
wh = wxh.split(' ')
print(wh)
print('[0]: ', wh[0])
w = wh[0]
print('[1]: ', wh[1])
h = wh[1]
print(int(w), int(h))