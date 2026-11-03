import sqlite3

DB_NAME = "tasks.db"

#1. Connect to database
def get_connection():
    return sqlite3.connect(DB_NAME)


# 2. Creat DataBase Table
def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    #Task Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT,
            priority TEXT DEFAULT 'medium',
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURENT_TIMESTAMP
            )
            """)

# Chat History table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEST NOT NULL,
            role TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )

""")

    conn.commit()
    conn.close()


print("Database initialized successfully!")
