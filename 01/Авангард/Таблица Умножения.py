def table():
    while True:
        num = input("Введите целое число (или 'exit' для выхода): ")
        if num.lower() == 'exit':
            print("Выход из программы...")
            break  # Прерываем бесконечный цикл
        try:
            num = int(num)
            for i in range(1,11):
                print(f'{num} x {i} = {num * i }')
            print()  # Пустая строка для разделения таблиц
        except ValueError:
            print("Пожалуйста, введите корректное целое число или 'exit'.\n")


table()