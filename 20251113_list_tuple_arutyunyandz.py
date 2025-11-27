#Есть изначально пустой список phrases.
#Напишите программу, по которой:
#- компьютер сначала запрашивает у пользователя 10 фраз
#  и помещает каждую фразу в список phrases;
#- потом компьютер запрашивает у пользователя целое
#  число N;
#- далее компьютер выводит построчно фразы из спика phrases,
#  но только те, чья длина больше, либо равна N.#\

list_phrases = []

scroll_through = 10
for i in range (scroll_through):
    phrases = input("Введите фразу номер %i:" %(i+1))
    list_phrases.append(phrases)
print()

num = input("Введите целое число(цифровым значением):").strip()
num = int(num)
print()

for phrases in list_phrases:
    if len(phrases) >= num:
        print(phrases, end = ", ")
print()

#Всё то же, что и на 10 баллов, но теперь:
#- есть ещё изначально пустой список filtered_phrases
#  (отфильтрованные фразы);
#- компьютер копирует из списка phrases в список
#  filtered_phrases такие фразы, длины которых больше,
#  либо равны N;
#- и далее компьютер выводит построчно содержимое списка
#  filtered_phrases.

filtered_phrases = []

for phrases in list_phrases:
    if len(phrases) >= num:
        filtered_phrases.append(phrases)
        print(phrases, end = ", ")

