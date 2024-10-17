#Написать анонимную функцию для сложения двух цифр
numbers = lambda num1, num2: num1 + num2

#Пример использования
num1 = int(input("Введите первую цифру:"))
num2 = int(input("Введите вторую цифру:"))

print(f"Сумма: {numbers(num1, num2)}")