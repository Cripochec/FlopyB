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
        logging.error(f"No connecting to database: {e}")
        return None


# Функция добавления таблиц
def add_tables(con):
    try:
        cur = con.cursor()

        create_table_query = '''
            CREATE TABLE IF NOT EXISTS account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            pas TEXT NOT NULL
            );
            '''
        cur.execute(create_table_query)

        con.commit()
        cur.close()
        con.close()
    except sqlite3.Error as e:
        logging.error(f"Tables are not added to the database: {e}")
        return None


# Функция добавления новых аккаунтов
def add_new_account(con, login, pas):
    try:
        cur = con.cursor()
        add_data_quary = "INSERT INTO account (login, pas) VALUES (?, ?)"

        cur.execute(add_data_quary, (login, pas))
        con.commit()
        cur.close()
    except sqlite3.Error as e:
        logging.error(f"The data is not entered into the 'account' table: {e}")




#Промежуточное получение
def get_all_logins(con):
    try:
        cur = con.cursor()
        get_all_login_quary = "SELECT login FROM account"

        cur.execute(get_all_login_quary)
        logins = cur.fetchall()
        cur.close()
        return [login[0] for login in logins]
    except sqlite3.Error as e:
        logging.error(f"Error fetching logins from 'account' table: {e}")
        return []


def get_password_by_login(con, login):
    try:
        cur = con.cursor()
        get_password_by_login_query = "SELECT id, pas FROM account WHERE login = ?"

        cur.execute(get_password_by_login_query, (login,))
        result = cur.fetchone()
        cur.close()

        if result:
            return result  # Возвращаем кортеж (id, pas)
        else:
            return "CODE13"
    except sqlite3.Error as e:
        logging.error(f"Error fetching password for login '{login}': {e}")
        return None



#
# con = connect_db(database_name)
# print(get_all_logins(con))
# print(get_password_by_login(con, "Андрей"))
