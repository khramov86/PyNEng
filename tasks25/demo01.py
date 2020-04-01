import sqlite3

db = sqlite3.connect('.\\dhcp_snooping.db')
# Переменная conn - это объект, который представляет реальное соединение с БД. Благодаря функции type, можно выяснить
# экземпляром какого класса является объект conn:
# print(type(db))
# db.in_transaction проверить, был ли коммит (возвращает True или False)
def init_table():
    db.execute("""
    create table dhcp (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mac TEXT NOT NULL,
            ip TEXT NOT NULL,
            interface text NOT NULL
                )""")

    db.execute("""
    alter table dhcp add vlan TEXT
                """)


query = 'insert into dhcp (mac, ip, vlan, interface) values (?, ?, ?, ?)'


# Выборка из базы
result = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dhcp'").fetchone()
# Если есть поле - тип будет tuple
# print(type(result))
if result is None:
    print("Инициализирую таблицу")
    init_table()
else:
    db.execute(query, ('0000.1111.7777', '10.255.1.1', '10', 'Gi0/7'))
    # Здесь метод вернет True
    print(db.in_transaction)
    db.execute("commit")
    # Здесь метод вернет False
    print(db.in_transaction)
db.close()

# print(db.in_transaction)
