import psycopg2
from ks_db.supplies.shets import read_table
from ks_db.supplies.cbr import dollar_rate
from datetime import datetime
CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '1gmOeYU2Z-UL5RAfBxNgaecCfjMdM9bvLi5knCqVqNjs'

# Подключение к существующей базе данных
connection = psycopg2.connect(user="postgres",
                              password="0111",
                              host="127.0.0.1",
                              port="5432",
                              database="kanalservice")

cursor = connection.cursor()
print("Информация о сервере PostgreSQL")
print(connection.get_dsn_parameters(), "\n")
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("Вы подключены к - ", record, "\n")


def create_table():
    create_table_query = '''CREATE TABLE ks_db
                        (id INTEGER PRIMARY KEY,
                        ord TEXT NOT NULL,
                        price REAL,
                        rub REAL,
                        delivery_time DATE); '''
    cursor.execute(create_table_query)
    print(f'Таблица создана')
    connection.commit()


def del_table():
    delete_table = "DROP TABLE ks_db"
    cursor.execute(delete_table)
    print('Таблица удалена')
    connection.commit()


def insert_data():
    sheet_data = read_table(spreadsheet_id)
    dollar_cource = dollar_rate()
    for data in sheet_data[1:]:
        date = datetime.strptime(data[3], '%d.%m.%Y')
        query = f"""INSERT INTO ks_db (id, ord, price, rub, delivery_time)
                    VALUES ({data[0]}, {data[1]}, {data[2]}, {int(data[2])*dollar_cource}, (%s))"""
        cursor.execute(query, (date,))
        connection.commit()
        print("1 запись успешно вставлена")


def prnt_data():
    cursor.execute("SELECT * from ks_db")
    record = cursor.fetchall()
    print("Результат", record)


#####
if connection:
    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")
