import sqlite3 as sql

directory = "database/contacts.db"


def main():
    # Connecting to the database
    conn = sql.connect(directory)

    # Cursor for sql queries
    cursor = conn.cursor()

    # QUERY
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(60) NOT NULL,
        phone VARCHAR(20) NOT NULL,
        email VARCHAR(50),
        address VARCHAR(100)
    );
    ''')

    conn.commit()
    conn.close()
