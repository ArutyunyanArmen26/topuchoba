#Вывести на экран таблицу из 4 строк: 3 товара и сумма без использования цикла
product1 ="Карандаш"
price1 = 35
kollichestvo1 = 2

product2 = "Стёрка"
price2 = 30
kollichestvo2 = 1

product3 = "Ручка"
price3 = 40
kollichestvo3 = 2

sum = (price1 * kollichestvo1) + (price2 * kollichestvo2) + (price3 * kollichestvo3)

print(f"{'Товар':<10} {'Цена':<5} {'Кол-во':<7} {'Сумма':<7}")
print(f"{product1:<10} {price1:<5} {kollichestvo1:<7} {price1 * kollichestvo1:<7}")
print(f"{product2:<10} {price2:<5} {kollichestvo2:<7} {price2 * kollichestvo2:<7}")
print(f"{product3:<10} {price3:<5} {kollichestvo3:<7} {price3 * kollichestvo3:<7}")
print(f"{'Итого:':<10} {'':<5} {'':<7} {sum:<7}")