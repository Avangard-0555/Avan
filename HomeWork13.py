import sqlite3
#Создаю или подключаем к базе данных
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

#Создаю таблицы для клиентов 
cursor.execute("""CREATE TABLE  IF NOT EXISTS clients(id INTEGER PRIMARY KEY AUTOINCREMENT, name  TEXT NOT NULL, phone TEXT UNIQUE NOT NULL, balance REALL DEFAULT 0.0)""")
#Регистрация клиента 
def register_client(name, phone):
    cursor.execute("INSERT INTO clients (name, phone)")
    conn.comit()
#Поиск клиента по имени и телефону
def serch_client(name, phone):
    cursor.execute("SELECT * FROM clients WHERE name = ? AND  phone = ?", (name, phone))
    return cursor.fetchone()
#Пополнение Баланса
def deposit(phone, amount):
    cursor.execute("UPDATE clients SET balance = balance + ? WHERE phone = ?", (amount, phone))
    conn.comit()
#Снятие  денег с баланса 
def withdraw(phone, amount):
    cursor.execute("SELECT balance FROM clients WHERE phone = ?", (phone,))
    balance = cursor.fetchone()[0]
    if balance >= amount:
        cursor.execute("UPDATE clients SET balance = balance - ? WHERE phone = ?", (amount, phone))
        conn.commit()
    else:
        print("Отмена транзакции у вас не достаточно средств")

#Просмотр Баланса
def  check_balance(phone):
    cursor.execute("SELECT balance FROM clients WHERE phone = ?", (phone,))
    balance = cursor.fetchone()[0]
    future_value = balance * (1 + rate / 100) ** (months / 12)
    return future_value

#Примеры использования
register_client("Алеексей Иванов", "+799900011220")
deposit("+799900011220", 1000)
withdraw("799900011220", 300)
print("Текущий баланс:", check_balance("799900011220"))
print("Баланс через 12 месяцев:", calculate_deposit("799900011220", 12))
conn.close


ТАБЛИЦА ДЛЯ СТУДЕНТОВ


#Таблица для студентов
import sqlite3
#Подключение к базе данных или создание новой
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
#Создание таблицы "students"
cursor.execute("""CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER, garde TEXT)""")
#Вставка записей в таблицу "students"
def insert_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
#Получение информации о студенте по имени
def get_student_by_name(name):
    cursor.execute("SELECT name, age, grade FROM students WHERE name = ?",(name,))
    return cursor.fetchone
#Обновление оценки студента
def update_student_grade(name, new_grade):
    cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade, name))
    conn.commit()
#Удаление студента
def delete_student(name):
    cursor.execute("DELETE FROM students WHERE name = ?", (name))
    conn.commit()
    
#Пример использования 
insert_student("Иван Иванов", 20, "B")
insert_student("Маша Саша", 19, "A")
print(get_student_by_name("Иван Иванов"))
update_student_grade("Иван Иванов", "C+")
delete_student("Маша Саша")
conn.close()





















        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

