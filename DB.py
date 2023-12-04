import sqlite3
import logging
from CONST import database_name

# Настройка логирования
logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d.%m.%Y / %H:%M:%S')


# Функция подключения к базе данных
def connect_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
        return None

# Функция вставки данных
def insert_data(conn, table, data):
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {table} VALUES (?, ?, ?)", data)
        conn.commit()
        logging.info("Данные успешно вставлены.")
    except sqlite3.Error as e:
        logging.error(f"Ошибка вставки данных: {e}")

# Функция обновления данных
def update_data(conn, table, set_clause, where_clause):
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {table} SET {set_clause} WHERE {where_clause}")
        conn.commit()
        logging.info("Данные успешно обновлены.")
    except sqlite3.Error as e:
        logging.error(f"Ошибка обновления данных: {e}")

# Пример использования функций
if __name__ == "__main__":
    conn = connect_db(database_name)

    if conn:
        # Пример вставки данных
        insert_data(conn, 'users', (1, 'John Doe', 25))

        # Пример обновления данных
        update_data(conn, 'users', 'age=30', 'name="John Doe"')

        # Закрытие соединения с базой данных
        conn.close()
