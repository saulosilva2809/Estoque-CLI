import sqlite3


DB_NAME = 'database/stock.db'

def get_connection():
    connection = sqlite3.connect(DB_NAME)

    # faz com que os resultados sejam acessíveis por nome:
    # row['name']
    connection.row_factory = sqlite3.Row

    return connection
