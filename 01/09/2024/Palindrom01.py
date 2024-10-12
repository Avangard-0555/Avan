slovo = input("Введите слово палиндром:")

eto_polindrom = True

for i in range(len(slovo) // 2): #123321
    if slovo[i].lower() != slovo[-(i+1)].lower():
        eto_polindrom = False
        break

if eto_polindrom:
    print("да")
else:
    print("no")

