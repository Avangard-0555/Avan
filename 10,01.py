# Базовый класс Транспортное средство
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"Марка: {self.brand}, Год выпуска: {self.year}"

# Подкласс Автомобиль
class Car(Vehicle):
    def __init__(self, brand, year, doors, engine_type):
        super().__init__(brand, year)
        self.doors = doors           # Количество дверей
        self.engine_type = engine_type  # Тип двигателя (например, бензиновый, дизельный)

    # Переопределение метода для автомобиля
    def display_info(self):
        return (f"Автомобиль {self.brand}, Год выпуска: {self.year}, "
                f"Двери: {self.doors}, Тип двигателя: {self.engine_type}")

# Подкласс Мотоцикл
class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_capacity, has_sidecar):
        super().__init__(brand, year)
        self.engine_capacity = engine_capacity  # Объем двигателя
        self.has_sidecar = has_sidecar          # Есть ли коляска (True/False)

    # Переопределение метода для мотоцикла
    def display_info(self):
        sidecar_info = "с коляской" if self.has_sidecar else "без коляски"
        return (f"Мотоцикл {self.brand}, Год выпуска: {self.year}, "
                f"Объем двигателя: {self.engine_capacity}cc, {sidecar_info}")

# Создание объектов автомобиля и мотоцикла
car = Car("Toyota", 2020, 4, "Бензиновый")
motorcycle = Motorcycle("Harley-Davidson", 2018, 1200, False)

# Вызов методов display_info() и вывод информации на экран
print(car.display_info())
print(motorcycle.display_info())