ids = [] # Пустой список
print("ids:", ids)

ids.append(1232) # Добавляет новый элемент в конец списка
print("ids:", ids)

ids.append(5)
ids.append(3)
print("ids:", ids)

print("Длина списка ids:", len(ids)) # len - показывает сколько переменных в списке

ids.append("Q")
print("ids:", ids)

print("Длина списка ids:", len(ids))



pet_names = []

for i in range(3):
    name = input("Введите имя питомца, варинат %i:" %(i + 1))
    pet_names.append(name)
print("Ваш список имён для питомца:", pet_names)

print("Ещё раз ваш список питомцев")
for name in pet_names: # Перебираем элементы списка
    print(name, end = ", ")
    
print("И ещё раз ваш список питомцев:", *pet_names) # * - вынимает элементы из списка

    

