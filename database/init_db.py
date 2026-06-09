from pathlib import Path

from database.connection import get_connection


def init_database():
    conn = get_connection()

    schema_path = Path('database/schema.sql')

    with open(schema_path, encoding='utf-8') as file:
        conn.executescript(file.read())

    conn.commit()
    conn.close()
