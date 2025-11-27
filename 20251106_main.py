min_temperature_celcius = 15
max_temperature_celcius = 30 

is_program_work = True
is_choice_wrong = False
is_temperature_high = False
is_temperature_low = False 
temperature_celsius = 20

while is_program_work:
    print("[Пульт температуры]")
    print("")
    print("Текущая температура: %i" % temperature_celsius)
    print("")
    print("1 - + градус")
    print("2 - - градус")
    print("0 - выход")
    print("")
    
    if is_choice_wrong:
        print("Ошибка: некорректный ввод")
        print("")
    if is_temperature_low:
        print("Предупреждение: сделать тепмературу ниже нельзя")
        print("")
    if is_temperature_high:
        print("Предупреждение: сделать тепмературу выше нельзя")
        print("")
        
    print(">>> ", end = "")
    
    choice = input().strip() # strip - убирает символы которые мы укажем
    
    if choice == "0":
        print("[ПУЛЬТ ТЕМПЕРАТУРЫ]")
        print("")
        print("Вы точно хотите выйти?")
        print("")
        print("1 - Нет! Работать дальше")
        print("0 - Да! Хочу выйти из программы")
        print("")
        print(">>> ", end = "")

        choise_2 = input().strip()

    
    is_choice_wrong = False
    is_temperature_high = False
    is_temperature_low = False 
    
    if choice == "0":
        if choise_2 == "0":
            is_program_work = False 
        elif choise_2 == "1":
            is_program_work = True
    elif choice == "1":
        if temperature_celsius < max_temperature_celcius:
            temperature_celsius += 1
        else:
            is_temperature_high = True
        
    elif choice == "2":
        if temperature_celsius > min_temperature_celcius:
            temperature_celsius -= 1
        else:
            is_temperature_low = True
        
    else:
        is_choice_wrong = True
        