
# Создаю переменную = int - целые числа - (input"введите число для табл умнж: ") :-закрыл
first_number = int(input("Ввведите число для таблицы умножения: "))
print(f"Таблица умножени для числа {first_number}: ")

for i in range(1,11):
    print(f"{first_number} * i = {first_number * i}")


