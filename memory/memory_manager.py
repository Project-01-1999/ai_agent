import sqlite3
from pathlib import Path


class MemoryManager:

    def __init__(self):

        db_path = Path(__file__).parent / "memory.db"

        self.connection = sqlite3.connect(db_path)

        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memory (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                key TEXT UNIQUE,

                value TEXT

            )
        """)
        
    def remember(self, key, value):

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO memory (key, value)
            VALUES (?, ?)
            """,
            (key, value)
        )

        self.connection.commit()

        return f"Remembered '{key}'."

    def recall(self, key):

        self.cursor.execute(
            """
            SELECT value FROM memory
            WHERE key = ?
            """,
            (key,)
        )

        result = self.cursor.fetchone()

        if result:
            return result[0]

        return None

    def forget(self, key):

        self.cursor.execute(
            """
            DELETE FROM memory
            WHERE key = ?
            """,
            (key,)
        )

        self.connection.commit()

        return f"Forgot '{key}'."