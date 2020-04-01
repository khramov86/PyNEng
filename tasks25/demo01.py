import sqlite3

db = sqlite3.connect('.\\dhcp_snooping.db')
# Переменная conn - это объект, который представляет реальное соединение с БД. Благодаря функции type, можно выяснить
# экземпляром какого класса является объект conn:
print(type(db))
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
db.execute(query, ('0000.1111.7777', '10.255.1.1', '10', 'Gi0/7'))
db.execute("commit")
db.close()

# print(db.in_transaction)
