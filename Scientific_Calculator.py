# Scientific Calculator 

import math
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

# Basic Operations for calculater
def add(a, b):
    result = a + b
    _store_in_db("Addition", a, b, result)
    return result

def subtract(a, b):
    result = a - b
    _store_in_db("Subtraction", a, b, result)
    return result

def multiply(a, b):
    result = a * b
    _store_in_db("Multiplication", a, b, result)
    return result

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    result = a / b
    _store_in_db("Division", a, b, result)
    return result

# Scientific Operations for calculater
def square_root(a):
    if a < 0:
        return "Error! Square root of negative number."
    result = math.sqrt(a)
    _store_in_db("Square Root", a, None, result)
    return result

def power(a, b):
    result = math.pow(a, b)
    _store_in_db("Power", a, b, result)
    return result

def sine(angle):
    result = math.sin(math.radians(angle))
    _store_in_db("Sine", angle, None, result)
    return result

def cosine(angle):
    result = math.cos(math.radians(angle))
    _store_in_db("Cosine", angle, None, result)
    return result

def tangent(angle):
    result = math.tan(math.radians(angle))
    _store_in_db("Tangent", angle, None, result)
    return result

def logarithm(a, base=10):
    if a <= 0:
        return "Error! Logarithm of non-positive number."
    result = math.log(a, base)
    _store_in_db("Logarithm", a, base, result)
    return result

# Store calculation in Data Base
def _store_in_db(operation, input1, input2, result):
    cursor.execute('''
        INSERT INTO history (operation, input1, input2, result)
        VALUES (?, ?, ?, ?)
    ''', (operation, input1, input2, result))
    conn.commit()

# get the  calculation history from Data Base
def get_history():
    cursor.execute('SELECT * FROM history')
    return cursor.fetchall()

# Clear calculation history
def clear_history():
    cursor.execute('DELETE FROM history')
    conn.commit()
