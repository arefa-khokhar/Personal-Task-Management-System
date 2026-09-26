from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

import sqlite3
from datetime import date


app = Flask(__name__)

app.secret_key = "personal-task-management-secret-key"

DATABASE = "tasks.db"


# ---------------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------------

def get_db_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


# ---------------------------------------------------
# CREATE DATABASE
# ---------------------------------------------------

def init_db():

    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            description TEXT,

            category TEXT NOT NULL DEFAULT 'General',

            priority TEXT NOT NULL DEFAULT 'Medium',

            status TEXT NOT NULL DEFAULT 'Pending',

            due_date TEXT,

            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()

    conn.close()


# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------

@app.route("/")
def home():

    # Get filter values from URL
    search = request.args.get("search", "").strip()

    status = request.args.get("status", "All")

    priority = request.args.get("priority", "All")

    category = request.args.get("category", "All")


    conn = get_db_connection()


    # ------------------------------------------------
    # BUILD TASK QUERY
    # ------------------------------------------------

    query = """
        SELECT *
        FROM tasks
        WHERE 1 = 1
    """

    parameters = []


    # Search
    if search:

        query += """
            AND (
                title LIKE ?
                OR description LIKE ?
            )
        """

        parameters.append(f"%{search}%")

        parameters.append(f"%{search}%")


    # Status filter
    if status != "All":

        query += """
            AND status = ?
        """

        parameters.append(status)


    # Priority filter
    if priority != "All":

        query += """
            AND priority = ?
        """

        parameters.append(priority)


    # Category filter
    if category != "All":

        query += """
            AND category = ?
        """

        parameters.append(category)


    # Newest tasks first
    query += """
        ORDER BY id DESC
    """


    tasks = conn.execute(
        query,
        parameters
    ).fetchall()


    # ------------------------------------------------
    # GET CATEGORIES
    # ------------------------------------------------

    categories = conn.execute("""
        SELECT DISTINCT category
        FROM tasks
        ORDER BY category
    """).fetchall()


    # ------------------------------------------------
    # DASHBOARD STATISTICS
    # ------------------------------------------------

    total = conn.execute("""
        SELECT COUNT(*)
        FROM tasks
    """).fetchone()[0]


    pending = conn.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'Pending'
    """).fetchone()[0]


    in_progress = conn.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'In Progress'
    """).fetchone()[0]


    completed = conn.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE status = 'Completed'
    """).fetchone()[0]


    # ------------------------------------------------
    # OVERDUE TASK COUNT
    # ------------------------------------------------

    today = date.today().isoformat()


    overdue = conn.execute("""
        SELECT COUNT(*)
        FROM tasks
        WHERE due_date IS NOT NULL
        AND due_date != ''
        AND due_date < ?
        AND status != 'Completed'
    """, (today,)).fetchone()[0]


    conn.close()


    # ------------------------------------------------
    # SEND DATA TO HTML
    # ------------------------------------------------

    return render_template(
        "index.html",

        tasks=tasks,

        categories=categories,

        search=search,

        selected_status=status,

        selected_priority=priority,

        selected_category=category,

        today=today,

        total=total,

        pending=pending,

        in_progress=in_progress,

        completed=completed,

        overdue=overdue
    )


# ---------------------------------------------------
# ADD TASK
# ---------------------------------------------------

@app.route("/add", methods=["POST"])
def add_task():

    title = request.form.get("title", "").strip()

    description = request.form.get(
        "description",
        ""
    ).strip()

    category = request.form.get(
        "category",
        "General"
    ).strip()

    priority = request.form.get(
        "priority",
        "Medium"
    )

    due_date = request.form.get(
        "due_date",
        ""
    )


    # Validate title
    if not title:

        flash(
            "Task title is required.",
            "error"
        )

        return redirect(url_for("home"))


    # Default category
    if not category:

        category = "General"


    conn = get_db_connection()


    conn.execute("""
        INSERT INTO tasks
        (
            title,
            description,
            category,
            priority,
            status,
            due_date
        )

        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        title,
        description,
        category,
        priority,
        "Pending",
        due_date
    ))


    conn.commit()

    conn.close()


    flash(
        "Task added successfully!",
        "success"
    )


    return redirect(url_for("home"))


# ---------------------------------------------------
# EDIT TASK
# ---------------------------------------------------

@app.route(
    "/edit/<int:task_id>",
    methods=["GET", "POST"]
)
def edit_task(task_id):

    conn = get_db_connection()


    task = conn.execute("""
        SELECT *
        FROM tasks
        WHERE id = ?
    """, (task_id,)).fetchone()


    # Task doesn't exist
    if task is None:

        conn.close()

        flash(
            "Task not found.",
            "error"
        )

        return redirect(url_for("home"))


    # ------------------------------------------------
    # UPDATE TASK
    # ------------------------------------------------

    if request.method == "POST":

        title = request.form.get(
            "title",
            ""
        ).strip()

        description = request.form.get(
            "description",
            ""
        ).strip()

        category = request.form.get(
            "category",
            "General"
        ).strip()

        priority = request.form.get(
            "priority",
            "Medium"
        )

        status = request.form.get(
            "status",
            "Pending"
        )

        due_date = request.form.get(
            "due_date",
            ""
        )


        # Validate title
        if not title:

            conn.close()

            flash(
                "Task title is required.",
                "error"
            )

            return redirect(
                url_for(
                    "edit_task",
                    task_id=task_id
                )
            )


        if not category:

            category = "General"


        conn.execute("""
            UPDATE tasks

            SET
                title = ?,
                description = ?,
                category = ?,
                priority = ?,
                status = ?,
                due_date = ?

            WHERE id = ?
        """, (
            title,
            description,
            category,
            priority,
            status,
            due_date,
            task_id
        ))


        conn.commit()

        conn.close()


        flash(
            "Task updated successfully!",
            "success"
        )


        return redirect(url_for("home"))


    conn.close()


    return render_template(
        "edit.html",
        task=task
    )


# ---------------------------------------------------
# MARK TASK AS COMPLETED
# ---------------------------------------------------

@app.route(
    "/complete/<int:task_id>",
    methods=["POST"]
)
def complete_task(task_id):

    conn = get_db_connection()


    conn.execute("""
        UPDATE tasks

        SET status = 'Completed'

        WHERE id = ?
    """, (task_id,))


    conn.commit()

    conn.close()


    flash(
        "Task marked as completed!",
        "success"
    )


    return redirect(url_for("home"))


# ---------------------------------------------------
# DELETE TASK
# ---------------------------------------------------

@app.route(
    "/delete/<int:task_id>",
    methods=["POST"]
)
def delete_task(task_id):

    conn = get_db_connection()


    conn.execute("""
        DELETE FROM tasks

        WHERE id = ?
    """, (task_id,))


    conn.commit()

    conn.close()


    flash(
        "Task deleted successfully.",
        "success"
    )


    return redirect(url_for("home"))


# ---------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------

if __name__ == "__main__":

    init_db()

    app.run(debug=True)
