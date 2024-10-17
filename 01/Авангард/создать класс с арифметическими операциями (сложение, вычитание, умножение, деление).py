class Calculator:
    def __init__(self, a, b):
        self.a = int(input("Введите число: "))
        self.b = int(input("Введите число: "))
    def slojenie (self,):
        return self.a + self.b
    def vichitanie (self):
        return self.a - self.b
    def umnojenie(self):
        return self.a * self.b
    def delenie(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Деление на ноль невозможно"


calc = Calculator(0, 0)


print(f"Сложение: {calc.slojenie()}")
print(f"Вычитание: {calc.vichitanie()}")
print(f"Умножение: {calc.umnojenie()}")
print(f"Деление: {calc.delenie()}")