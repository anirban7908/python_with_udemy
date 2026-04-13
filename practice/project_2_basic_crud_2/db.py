import sqlite3


class Storage:
    _conn = None

    def __init__(self):
        self._conn = sqlite3.connect("database.db")

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                salary REAL,
                is_active BOOLEAN,
                notes TEXT
            )
        """

        cursor = self._conn.cursor()
        cursor.execute(query)
        self._conn.commit()

    def insert_user(self, data):
        query_str = """
            INSERT INTO users (name, age, salary, is_active, notes)
            VALUES (?, ?, ?, ?, ?)
        """
        try:
            cursor = self._conn.cursor()

            cursor.execute(
                query_str,
                (
                    data.get("name"),
                    data.get("age"),
                    data.get("salary"),
                    data.get("is_active"),
                    data.get("notes"),
                ),
            )
            process = self._conn.commit()

            if cursor.rowcount > 0:
                return [{"status": True, "message": "Data inserted"}]
            else:
                return [{"status": False, "message": "Data insertion failed!"}]
        except sqlite3.Error as e:
            return [{"status": False, "message": f"Database error occurred: {e},"}]

    def update_user(self, id, data):
        query_str = f"""
            UPDATE users SET {data['col_name']} = ?
            WHERE id = ?
        """

        try:
            cursor = self._conn.cursor()
            cursor.execute(query_str, (data["col_value"], data["user_id"]))
            process = self._conn.commit()

            if cursor.rowcount > 0:
                return [{"status": True, "message": "Data Updated"}]
            else:
                return [{"status": False, "message": "Data updation failed!"}]

        except sqlite3.Error as e:
            return [{"status": False, "message": f"Database error occurred: {e},"}]

    def delete_user(self, user_id):
        query_str = """DELETE FROM users WHERE id = ?"""
        try:
            cursor = self._conn.cursor()
            cursor.execute(query_str, (user_id,))
            process = self._conn.commit()
            if cursor.rowcount > 0:
                return [{"status": True, "message": "Data Updated"}]
            else:
                return [{"status": False, "message": "Data updation failed!"}]
        except sqlite3.Error as e:
            return [{"status": False, "message": f"Database error occurred: {e},"}]

    def show_all_users(self):
        query_str = """SELECT * FROM users;"""
        try:
            cursor = self._conn.cursor()
            cursor.execute(query_str)
            records = cursor.fetchall()
            if records:
                return [{"status": True, "message": "Data Updated", "data": records}]
            else:
                return [{"status": False, "message": "Data updation failed!"}]
        except sqlite3.Error as e:
            return [{"status": False, "message": f"Database error occurred: {e},"}]

    def show_specific_user(self, user_data):
        query_str = f"""SELECT * FROM users WHERE {user_data['col_name']} = ?;"""
        try:
            cursor = self._conn.cursor()
            cursor.execute(query_str, (user_data["col_val"],))
            records = cursor.fetchall()
            if records:
                return [{"status": True, "message": "Data Updated", "data": records}]
            else:
                return [{"status": False, "message": "Data updation failed!"}]
        except sqlite3.Error as e:
            return [{"status": False, "message": f"Database error occurred: {e},"}]

    def kill_conn(self):
        self._conn.close()
