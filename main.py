from DB import connect_db, add_tables
import CONST

def start_settings():
    con = connect_db(CONST.database_name)
    add_tables(con)


if __name__ == '__main__':
    start_settings()
