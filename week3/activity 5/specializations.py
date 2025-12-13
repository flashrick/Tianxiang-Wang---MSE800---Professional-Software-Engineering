from database import Database


class Specializations:
    """Helper that builds the specializations table."""

    def __init__(self, db: Database) -> None:
        # Share the database connection for reuse
        self.db = db

    def create_table(self) -> None:
        # Create the specialization table so doctors can reference it
        self.db.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS specializations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
            """
        )

    def add(self, name: str) -> int:
        # Insert one specialization row and return the id
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO specializations(name) VALUES (?)",
            (name,),
        )
        self.db.commit()
        return cursor.lastrowid
