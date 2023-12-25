import sqlite3

#________________Query Str________________
CREATE_TABLE_SHOP = "CREATE TABLE IF NOT EXISTS tbl_shop (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,price INTEGER,\
                                                      star INTEGER,garanty INTEGER)"
SELECT_ALL_SHOP = "SELECT * FROM tbl_shop"
SELECT_GARANTY_SHOP = "SELECT * FROM tbl_shop WHERE garanty = 1" 
SELECT_GARANTY_NOT_NULL_SHOP = "SELECT * FROM tbl_shop WHERE garanty = 1 AND name IS NOT NULL" 
DELETE_ROW_SHOP = "DELETE FROM tbl_shop WHERE name = ?"
DELETE_TABLE_SHOP = "DROP TABLE tbl_shop"
SEARCH_SHOP = "SELECT * FROM tbl_shop WHERE name = ?"
INSERT_INTO_SHOP = "INSERT INTO tbl_shop (name,price,star,garanty) VALUES (?,?,?,?)"


#________________Connect Method________________


def check_connection():
    connection = sqlite3.connect("djshop.db")
    return connection

#________________Query Method________________


def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE_SHOP)
        print("create_table")

def select_all_table(connection):
    with connection:
        return connection.execute(SELECT_ALL_SHOP).fetchall()



def delete_table(connection):
    with connection:
        connection.execute(DELETE_TABLE_SHOP)
        print("delete_table")

def insert_into_table_shop(connection,name,price,star,garanty):
    with connection:
        connection.execute(INSERT_INTO_SHOP,(name,price,star,garanty))
        print("inserted")


def search_into_table_shop(connection,name):
    with connection:
        return connection.execute(SEARCH_SHOP,(name,)).fetchall()      