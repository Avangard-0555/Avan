class room:
    def __init__(self, l, w):
        lenght = float(input("Введите длину комнаты: "))
        width = float(input("Введите ширину комнаты: "))
        area = lenght * width
        print(f"Площадь комнаты равна {area} кв.м")

calc_room = room(0, 0)