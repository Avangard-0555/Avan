# Словарь для хранения контактов
contacts = {}

# Бесконечный цикл для работы с меню
while True:
    print("Меню:")
    print("1. Добавить контакт")
    print("2. Изменить контакт")
    print("3. Удалить контакт")
    print("4. Показать все контакты")
    print("5. Выход")

    choice = input("Выберите действие: ")

    # Добавление нового контакта
    if choice == "1":
        name = input("Введите имя: ")
        number = input("Введите номер телефона: ")
        if name in contacts:
            print(f"Контакт с именем '{name}' уже существует!")
        else:
            contacts[name] = number
            print(f"Контакт '{name}' добавлен.")

    # Изменение существующего контакта
    elif choice == "2":
        name = input("Введите имя контакта для изменения: ")
        if name in contacts:
            new_phone = input(f"Введите новый номер телефона для '{name}': ")
            contacts[name] = new_phone
            print(f"Номер телефона для '{name}' обновлен.")
        else:
            print(f"Контакт с именем '{name}' не найден.")

    # Удаление контакта
    elif choice == "3":
        name = input("Введите имя контакта для удаления: ")
        if name in contacts:
            del contacts[name]
            print(f"Контакт '{name}' удален.")
        else:
            print(f"Контакт с именем '{name}' не найден.")

    # Показ всех контактов
    elif choice == "4":
        if contacts:
            print("Список контактов:")
            for name, phone in contacts.items():
                print(f"Имя: {name}, Телефон: {phone}")
        else:
            print("Список контактов пуст.")

    # Выход из программы
    elif choice == "5":
        print("Выход из системы.")
        break  # Выход из цикла

    # Если введено ошибочно
    else:
        print("Неверный ввод. Попробуйте снова.")