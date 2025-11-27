#        0123    4 не будет!
mystr = 'Wera'
print(len(mystr)) 
first = mystr[0]  # Обращение по индексу 
print(first)
# Написать программу, которая выводит все буквы слова: 
# 1. В столбик
print('Stolbik: ')
for symvol in mystr:
    print(symvol)

# 2. В строчку через пробел 
print('Строчка через пробел:  ')
for symvol in mystr:
    print(symvol, end=' ')
# 3. В столбик в обратном порядке 

print('\n Столбик в обратном порядке: ')
for i in range(len(mystr) - 1, -1, -1):
    print(mystr[i])
    
print('Столбик, но все буквы маленькие: ')
for symbol in mystr:
    print(symbol.lower())