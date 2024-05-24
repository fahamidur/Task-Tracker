import sqlite3

class TaskDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                start_date TEXT,
                deadline TEXT,
                status TEXT,
                priority INTEGER,
                payment REAL
            )''')

    def add_task(self, title, description, start_date, deadline, status, priority, payment):
        with self.conn:
            self.conn.execute('''
                INSERT INTO tasks (title, description, start_date, deadline, status, priority, payment)
                VALUES (?, ?, ?, ?, ?, ?, ?)''', (title, description, start_date, deadline, status, priority, payment))

    def get_all_tasks(self):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM tasks')
            return cursor.fetchall()

    def get_last_n_tasks(self, n):
        with self.conn:
            cursor = self.conn.execute('SELECT * FROM tasks ORDER BY id DESC LIMIT ?', (n,))
            return cursor.fetchall()

    def filter_tasks_by_date(self, start_date, end_date):
        with self.conn:
            cursor = self.conn.execute('''
                SELECT * FROM tasks WHERE start_date >= ? AND deadline <= ?''', (start_date, end_date))
            return cursor.fetchall()

    def update_task(self, task_id, title, description, start_date, deadline, status, priority, payment):
        with self.conn:
            self.conn.execute('''
                UPDATE tasks SET title = ?, description = ?, start_date = ?, deadline = ?, status = ?, priority = ?, payment = ?
                WHERE id = ?''', (title, description, start_date, deadline, status, priority, payment, task_id))

    def get_task_by_id(self, task_id):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            task = cursor.fetchone()
            return task if task else None

