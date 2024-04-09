# import sqlite3
#
# DATABASE_URL = 'clinica.db'
#
#
# def initialize_connection():
#     conn = sqlite3.connect(DATABASE_URL)
#     cursor = conn.cursor()
#     # create_database(cursor)
#     create_table(cursor)
#
#     return conn, cursor
#
#
# # def create_database(cursor):
# #     cursor.execute("SHOW DATABASES")
# #     temp = cursor.fetchall()
# #     databases = [item[0] for item in temp]
# #
# #     if "tutorial" not in databases:
# #         cursor.execute("CREATE DATABASE tutorial")
# #
# #     cursor.execute("USE tutorial")
#
#
# def create_table(cursor):
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Users (
#         id INTEGER PRIMARY KEY,
#         username TEXT NOT NULL,
#         email TEXT NOT NULL,
#         age INTEGER
#         )
#         ''')
#
#
# def login(cursor, data):
#     cursor.execute(f"""SELECT * FROM users WHERE email = '{data["email"]}'
#                        AND password = '{data["password"]}' """)
#
#     if cursor.fetchone() is not None:
#         return True
#     return False
#
#
# def register(cursor, conn, data):
#     print(data)
#
#     cursor.execute(f"""INSERT INTO users values(
#         NULL,
#         '{data["firstName"]}',
#         '{data["lastName"]}',
#         '{data["password"]}',
#         '{data["email"]}',
#         '{data["gender"]}',
#         '{data["age"]}',
#         '{data["address"]}'
#     )""")
#
#     conn.commit()
