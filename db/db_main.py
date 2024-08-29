import sqlite3
from db import queries

db = sqlite3.connect('db/db.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print("База данных SQLite3 подключена!")
    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    cursor.execute(queries.CREATE_TABLE_ZAKAZY)
    db.commit()


async def sql_insert_products(name, category, size, price, id_product, photo):
    cursor.execute(queries.INSERT_PRODUCTS, (
        name,
        category,
        size,
        price,
        id_product,
        photo
    ))
    db.commit()


async def sql_insert_zakazy(id_product, size, quantity, phone):
    cursor.execute(queries.INSERT_ZAKAZY, (
        id_product,
        size,
        quantity,
        phone
    ))
    db.commit()


