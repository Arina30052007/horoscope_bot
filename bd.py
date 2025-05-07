import sqlite3

connection = sqlite3.connect('statistic.db', check_same_thread=False)
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
zodiac TEXT NOT NULL
)
''')


def tgidregister(id, user, zodiac):
    try:
        cursor.execute('INSERT INTO Users (id, username, zodiac) VALUES (?, ?, ?)',
                       (id, user, zodiac))
        connection.commit()
    except Exception as e:
        print(e)
