import sqlite3
from time import time
from typing import Dict, Any

# Database file name
DB_NAME = "logs.db"

def init_db():
    """Initialize the database and create the logs table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time_agent TEXT NOT NULL,
            time_server TEXT NOT NULL,
            method TEXT NOT NULL,
            host TEXT NOT NULL,
            ip TEXT NOT NULL,
            layout TEXT,
            input TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_log(log: Dict[str, Any], method:str) -> bool:
    """Insert a log entry into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    time_server= time()
    print(f"Column used: {log['input']}")
    try:
        cursor.execute('''
            INSERT INTO logs (time_agent, time_server, method, host, ip, layout, input)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (log['time_agent'], time_server, method, log['host'], log['ip'], log['layout'], log['input']))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting log: {e}")
        return False
    finally:
        conn.close()
