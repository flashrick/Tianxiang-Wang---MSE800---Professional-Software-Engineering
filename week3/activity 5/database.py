import sqlite3
from pathlib import Path


class Database:
    """Lightweight wrapper around the sqlite3 connection."""

    def __init__(self, db_path: str) -> None:
        # Store file path so other helpers can reuse it
        self.db_path = Path(db_path)
        # Create the connection immediately for shared use
        self.connection = sqlite3.connect(self.db_path)

    def cursor(self):
        # Return a cursor to execute SQL statements
        return self.connection.cursor()

    def commit(self) -> None:
        # Persist pending changes to disk
        self.connection.commit()

    def close(self) -> None:
        # Close the connection when everything is done
        self.connection.close()
