# Создаём список контактов

names = ["Michael", "Jordan","Leyla"]
numbers = [991231111, 900999009, 55555555]
# Добавляем значение в переменyю name и number
name = str(input('Введите имя нового абонента:'))
number = str(input('Введите абонентский номер:'))
if number in numbers:
    print('Данный номер уже есть ')
else:
    names.append(name)
    numbers.append(number)
    print(f"Абонент {name} сохранён в контакты {number}")
    print(names,numbers)

# Изменение контакта
edit_name = input("Введите имя контакта которые хотите изменить: ")
if edit_name in names:
    index = names.index(edit_name)
    new_name = input("Введите новое имя: ")
    new_number = input("Введите новый номер: ")

    if new_name in names:
        print("Этот контакт уже существует!")
    elif new_number in numbers:
        print("Этот номер уже сушествует!")
    else:
        names[index] = new_name
        numbers[index] = new_number
        print(f"Контакт {edit_name} изменён на {new_name} с номером {new_number}.")
else:
    print("Контакт не найден")

# Удаление контакта
delete_name = input("Введите имя контакта которого хотите удалить: ")
if delete_name in names:
    index = names.index(delete_name)
    names.pop(index)
    numbers.pop(index)
    print(f"Контакт {delete_name} удалён.")
else:
    print("Контакт не найден")

print(names, numbers)
print(index)