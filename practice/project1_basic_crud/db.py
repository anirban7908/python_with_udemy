import sqlite3
import json
import uuid


def connect_db():
    conn = sqlite3.connect("database.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            salary REAL,
            is_active BOOLEAN,
            notes TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_user(data):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (name, age, salary, is_active, notes)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data.get("name"),
        data.get("age"),
        data.get("salary"),
        data.get("is_active"),
        data.get("notes")
    ))

    conn.commit()
    conn.close()

def get_users():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_user(user_id, name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET name = ?
        WHERE id = ?
    """, (name, user_id))

    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

    conn.commit()
    conn.close()