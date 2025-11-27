 #Компьютер запрашивает у пользователя 7 зветов радуги.
#Помещает их в список и выводит эти цвета из списка построчно



colors_rainbow = []

for i in range(7):
    color = input("Введите цвет радуги, варинат %i:" %(i + 1))
    colors_rainbow.append(color)
print()

print("Ваш список цветов радуги:")
print()
for color in colors_rainbow:
    print(color)
print()
    
color_index = 0

print("Ваш список цветов радуги:")
print()
for color in colors_rainbow:
    print(color_index, color)
    color_index += 1
print()
    
print("И ещё ваш список цветов радуги:")
print()
for color in (colors_rainbow): # или reversed
    print(color[-1::-1])

    

