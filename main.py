import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

def print_author():
    # Второй аргумент — значение по умолчанию, если AUTHOR не найден
    author = os.getenv("AUTHOR", "Не указано")
    print(f"Автор проекта: {author}")

# Вот эта часть раньше отсутствовала — она запускает функцию при запуске файла
if __name__ == "__main__":
    print_author()

