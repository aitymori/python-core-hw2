result = None
operand = None
operator = None
wait_for_number = True

    
while True:

    if operator == "=":
        print(f"Результат обрахунку: {result}")
        break        
    
    # Отримання першого значення

    while result == None:
        result = input("Введіть число: ")
        try:
            result = float(result)
            wait_for_number = False
        except ValueError:
            print(f"Значення {result} це не число. Спробуйте знову.")


    # Отримання й перевірка оператора 
    while wait_for_number == False:

        while True:
            operator = input("Введіть оператор (+ - * /) або '=' для завершення обрахунку: ")
            if operator == "=":
                break
            
            elif operator == "+" or operator == "-" or operator == "*" or operator == "/":
                wait_for_number = True
                break
            else:
                print(f"Значення {operator} - це не оператор. Спробуйте '+' '-' '*' '/' для виконання дії або '=' для виведення результату.")
        
        # Отримання числа
        while wait_for_number == True:
            operand = input("Введіть число: ")
            try:
                operand = float(operand)
                wait_for_number = False
            except ValueError:
                print(f"Значення {operand} це не число. Спробуйте знову.")        
        
        
        # Виконання дії (+ - * /)

        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result /= operand   
        elif operator == "=":
            break
