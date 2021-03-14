import sqlite3
def create_db():
    db_name = 'ProfileUser'
    query_create = '''CREATE TABLE UsersLastEntry (id_user INTEGER, text TEXT NOT NULL)'''

    sql_conn = sqlite3.connect(db_name)
    cursor = sql_conn.cursor()
    cursor.execute(query_create)
    sql_conn.commit()

    cursor.close()
    sql_conn.close()
