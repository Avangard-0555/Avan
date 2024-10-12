import nltk
from nltk.tokenize import word_tokenize
import sympy as sp
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import pylint.lint
import os

# Загрузим токенизатор для анализа текста
nltk.download('punkt')

class HomeworkAI:
    def __init__(self):
        pass

    def solve_math(self, equation):
        try:
            x = sp.Symbol('x')
            eq = sp.sympify(equation)
            solution = sp.solve(eq, x)
            return f"Решение уравнения {eq}: {solution}"
        except Exception as e:
            return f"Ошибка при решении: {str(e)}"

    def analyze_text(self, text):
        tokens = word_tokenize(text.lower())
        if "уравнение" in tokens:
            return "Это математическая задача."
        elif any(term in tokens for term in ["программирование", "код", "алгоритм", "сеть"]):
            return "Это задача по IT."
        else:
            return "Это текстовый вопрос."

    def analyze_code(self, code):
        # Создаем временный файл для анализа кода
        with open("temp_code.py", "w") as f:
            f.write(code)

        # Запускаем pylint и игнорируем ошибки
        try:
            results = pylint.lint.Run(["temp_code.py"], do_exit=False)  # type: ignore
            score = results.linter.stats['global_note']
            messages = results.linter.msgs
        except Exception as e:
            score = 0
            messages = [f"Ошибка при анализе кода: {str(e)}"]

        os.remove("temp_code.py")  # Удаляем временный файл
        return score, messages

# Создаем экземпляр ИИ
Ai = HomeworkAI()

# Токен, который я получил от BotFather
TELEGRAM_TOKEN = "7670538813:AAEPtgrWFywGsIDFSPpe3_9PaW0yLxhHwDA"  # Замените на свой токен

# Функция для команды /start
def start(update, context):
    update.message.reply_text(
        "Привет! Я AVANGARD ИИ помощник для домашки. Введите математическое уравнение или код для анализа."
    )

# Функция для обработки текстовых сообщений
def handle_message(update, context):
    user_message = update.message.text
    if "=" in user_message:  # Если пользователь ввел уравнение
        response = Ai.solve_math(user_message)
    elif user_message.startswith("```"):  # Если пользователь прислал код
        code = user_message.strip("```")
        score, messages = Ai.analyze_code(code)  # Анализ кода
        response = f"Оценка кода: {score}\n\nСообщения:\n"
        for msg in messages:
            response += f"{msg}\n"
    else:  # Иначе обрабатываем как текст
        response = Ai.analyze_text(user_message)

    update.message.reply_text(response)

# Основной код для запуска бота
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()