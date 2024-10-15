
# Module: Database Handler for  Calculator

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('calculator.db')
cursor = conn.cursor()

# Create a table to store calculation history if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY,
        operation TEXT,
        input1 REAL,
        input2 REAL,
        result REAL
    )
''')

def store_calculation(operation, input1, input2, result):
    cursor.execute('''
        INSERT INTO history (operation, input1, input2, result)
        VALUES (?, ?, ?, ?)
    ''', (operation, input1, input2, result))
    conn.commit()

def get_calculation_history():
    cursor.execute('SELECT * FROM history')
    return cursor.fetchall()

def clear_calculation_history():
    cursor.execute('DELETE FROM history')
    conn.commit()
