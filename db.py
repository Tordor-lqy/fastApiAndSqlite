import sqlite3

def initDb():
    # 创建SQLite数据库连接
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    # 创建订单表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            order_time DATETIME DEFAULT CURRENT_TIMESTAMP,
            order_status INTEGER DEFAULT 0,
            account TEXT,
            contact TEXT,
            password TEXT,
            note TEXT,
            order_amount REAL DEFAULT 0
        )
    ''')

    # 提交表结构更改
    conn.commit()

def getDb():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    return conn , cursor

def run():
    initDb()

if __name__ == '__main__':
    run()