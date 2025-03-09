import sqlite3

def db_manager_single(q):
    connection = sqlite3.connect('myshop.db')
    cursor = connection.cursor()
    cursor.execute(q)
    connection.commit()
    connection.close()

def db_manager_many(q, data):
    connection = sqlite3.connect('myshop.db')
    cursor = connection.cursor()
    cursor.executemany(q, data)
    connection.commit()
    connection.close()

def db_manager_read(q):
    connection = sqlite3.connect('myshop.db')
    cursor = connection.cursor()
    cursor.execute(q)
    return cursor.fetchall()



q = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL UNIQUE,
        full_name TEXT NOT NULL,
        password TEXT NOT NULL
    )
'''
# db_manager_single(q)


# Insert into users
q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES ('johndoe', 'John Doe', '123')
'''
# db_manager_single(q)


q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES ('mahdiwnrd', 'Mahdi Noordad', '1383')
'''
# db_manager_single(q)
    

data = [
    ('ali@gmail.com', 'Ali Akbari', '151'),
    ('sara@gmail.com', 'Sara Ahadi', '321'),
    ('ben@gmail.com', 'Ben Mira', '333'),
    ('saeed@gmail.com', 'Saeed Sobhan', '4444'),
    ('maryam@gmail.com', 'Maryam Imani', '1111'),

]
q = '''
    INSERT INTO users (user_name, full_name, password) VALUES(?, ?, ?)
'''
# db_manager_many(q, data)


q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES ('mohammadrad', 'Mohamad Rad', '138')
'''
# db_manager_single(q)


# table product
q = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price NUMERIC NOT NULL,
        description TEXT NULL default '',
        is_exist BOLLEAN NOT NULL default TRUE      
    )
'''
# db_manager_single(q)


data = [
    ('Tunna', 103),
    ('Rice', 205),
    ('Chips', 18),
    ('Bread', 10),
    ('Water', 7)

]
q = '''
    INSERT INTO products (name, price) 
    VALUES(?, ?)
'''
# db_manager_many(q, data)


q = '''
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_id INTEGER,
        quantity INTEGER NOT NULL,
        total REAL NOT NULL,
        created_at TEXT NOT NULL DEFAULT current_timestamp,
        updated_at TEXT NOT NULL DEFAULT current_timestamp,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
'''
# db_manager_single(q)


data = [
    (1, 1, 300, 1),
    (1, 3, 200, 1),
    (2, 2, 100, 1),
    (2, 3, 250, 1),
    (4, 4, 220, 1),
    (6, 2, 210, 1),
    (6, 4, 200, 1)
]
q = '''
    INSERT INTO invoices (user_id, product_id, total, quantity) 
    VALUES(?, ?, ?, ?)
'''
# db_manager_many(q, data)



# q = 'SELECT full_name FROM users'
# data = db_manager_read(q)

# for item in data:
#     print(item)


# q = 'SELECT product_id, user_id FROM invoices'
# data = db_manager_read(q)

# for item in data:
#     print(item)


# q = 'DELETE FROM invoices where id = 7'
# db_manager_single(q)


# q = '''
#     SELECT users.full_name, products.name
#     FROM users
#     INNER JOIN invoices on invoices.user_id = users.id
#     INNER JOIN products on invoices.product_id = products.id
# '''
# data = db_manager_read(q)

# for item in data:
#     print(item)


# q = '''
#     SELECT users.full_name, products.name
#     FROM users
#     INNER JOIN invoices on invoices.user_id = users.id 
#     INNER JOIN products on invoices.product_id = products.id
#     WHERE users.id = 1
# '''
# data = db_manager_read(q)

# for item in data:
#     print(item)


q = '''
    UPDATE users
    SET full_name = 'John Coe'
    WHERE id = 1
    LIMIT 3
'''
db_manager_single(q)





















