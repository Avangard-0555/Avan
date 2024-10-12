# Родительский класс Игрок
class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def display_info(self):
        return f"Игрок {self.name} под номером {self.number}"


# Подкласс Нападающий
class Forward(Player):
    def __init__(self, name, number):
        super().__init__(name, number)

    # Особенная фишка для нападающего
    def special_move(self):
        return f"{self.name} делает потрясающий удар по воротам!"


# Подкласс Защитник
class Defender(Player):
    def __init__(self, name, number):
        super().__init__(name, number)

    # Особенная фишка для защитника
    def special_move(self):
        return f"{self.name} блокирует атаку соперника!"


# Подкласс Полузащитник
class Midfielder(Player):
    def __init__(self, name, number):
        super().__init__(name, number)

    # Особенная фишка для полузащитника
    def special_move(self):
        return f"{self.name} мастерски передает мяч нападающему!"


# Подкласс Вратарь
class Goalkeeper(Player):
    def __init__(self, name, number):
        super().__init__(name, number)

    # Особенная фишка для вратаря
    def special_move(self):
        return f"{self.name} делает невероятный сэйв!"


# Пример использования классов

# Создаем игроков
forward = Forward("Лео Месси", 10)
defender = Defender("Серхио Рамос", 4)
midfielder = Midfielder("Кевин Де Брюйне", 17)
goalkeeper = Goalkeeper("Мануэль Нойер", 1)

# Выводим информацию о каждом игроке и их особую фишку
players = [forward, defender, midfielder, goalkeeper]

for player in players:
    print(player.display_info())
    print(player.special_move())
    print("------")