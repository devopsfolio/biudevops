import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def execute_query(self, query):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
                print("Запрос выполнен.")
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")

    def fetch_data(self, query):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")
            return []

# Пример использования:
db_manager = DatabaseManager("example.db")
db_manager.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
db_manager.execute_query("INSERT INTO users (name) VALUES ('Alice')")
data = db_manager.fetch_data("SELECT * FROM users")
print(data)
