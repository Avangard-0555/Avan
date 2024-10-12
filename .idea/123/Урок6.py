# создаю склад
all_products = {"картофель": 10, "морковь": 30}
while True:
    # создаю главное меню
    action = input("Выберите действие\n"
                   "1- Добавить продукт\n"
                   "2- Посмотреть продукты: ")
    # если я выбрал в главном меню "добавить"
    if action.lower() == "добавить":
        #запрашиваю название продукта
        name = input("Введите название продукта: ")
        #запрашиваю количество продукта
        count = int(input("Введите количество продукта: "))
        # проверяю есть ли такой товар на складе
        if name in all_products.keys():
            # добавляем к существующему количеству новое количество
            all_products[name] += count
            print("продукт обновлен")
        # а если такого товара нет, то просто добавляем
        elif name not in all_products.keys():
            all_products[name] = count
            print("продукт добавлен")
    # если в главном меню выбрали "посмотреть"
    elif action == "посмотреть":
        number = 0
        print("Товары на складе: ")
        for name, count in all_products.items():
            number += 1
            print(f"{number}. {name} - {count} кг")