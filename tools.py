from langchain.tools import tool
from database import get_connection

# TOOL 1: Creat new TASK

@tool
def create_task(title:str, due_date:str, priority:str) -> str:
    """Create a new tasks with title, dur date and priority."""

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """INSERT INTO tasks  (title, due_date, priority)
            VALUES (?, ?, ?)""",
            (title, due_date, priority)
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()

    return f"Task created successfully! Task ID: {task_id}"


#List Task 
@tool
def list_tasks(status: str = "pending") -> str:
    """Retrieve tasks filtered y status: pending or completed."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, due_date, priority, status FROM tasks WHERE status = ?",
        (status,)
    )
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        return f"NO {status} tasks found."
    return str(tasks)
#Tool 3 : Update task status
@tool
def update_task_status(task_id: int, status: str) -> str:
    """Update a tasks status to pending or completed using its task ID."""

    if status not in ["pending", "completed"]:
        return "Invalid status. Use pending or completed."

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        (status, task_id)
    )

    updated = cursor.rowcount
    conn.commit()
    conn.close()

    if updated == 0:
        return f"Task ID {task_id} not found."

    return f"Task {task_id} updated to {status} successfully!"

# Register all tools
tools = [create_task, list_tasks, update_task_status]
