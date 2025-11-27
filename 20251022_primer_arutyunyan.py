#Получить математический пример с клавиатуры, вычислить
import numexpr
primer = input('Введите математический пример:')
try:
    otvet = numexpr.evaluate(primer)
    print('Результат:', otvet)
except Exception as e:
    print('Ошибка: Некорректное выражение:', e)
