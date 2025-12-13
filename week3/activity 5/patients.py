from datetime import date
from database import Database


class Patients:
    """Helper for the patients table."""

    def __init__(self, db: Database) -> None:
        self.db = db

    def create_table(self) -> None:
        # Create the patients table with the fields from the ER diagram
        self.db.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                birth TEXT NOT NULL,
                gender TEXT NOT NULL
            )
            """
        )

    def add(self, name: str, email: str, phone: str, birth: str, gender: str) -> int:
        # Insert a patient record and return its id
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO patients(name, email, phone, birth, gender)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, email, phone, birth, gender),
        )
        self.db.commit()
        return cursor.lastrowid

    def get_seniors(self) -> list[tuple]:
        # Return all patients older than 65 years
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT id, name, email, phone, birth, gender
            FROM patients
            WHERE birth <= date('now', '-65 years')
            """,
        )
        return cursor.fetchall()
