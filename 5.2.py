names = ["Pavel", "Jordan", "Sasha",]
names2 = [name for name in names if name[0].lower() == "P"]
print(names2)
user_input = input("Введите слово: ")
user_input = user_input.lower()
if user_input == user_input[::-1]:
    print("это палиндром!")