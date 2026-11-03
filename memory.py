
from database import get_connection


# 1. Save conversation message
def save_message(session_id, role, message):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """INSERT INTO chat_messages (session_id, role, messages)
           VALUES (?, ?, ?)""",
        (session_id, role, message)
    )

    conn.commit()
    conn.close()


# 2. Retrieve conversation history
def get_history(session_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """SELECT role, messages
           FROM chat_messages
           WHERE session_id = ?
           ORDER BY id ASC""",
        (session_id,)
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {"role": role, "content": message}
        for role, message in rows
    ]


# 3. Clear conversation history
def clear_history(session_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM chat_messages WHERE session_id = ?",
        (session_id,)
    )

    conn.commit()
    conn.close()
