from database import Database


class Doctors:
    """Helper for the doctors table."""

    def __init__(self, db: Database) -> None:
        self.db = db

    def create_table(self) -> None:
        # Create the doctors table with the fields from the ER diagram
        self.db.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL,
                birth TEXT NOT NULL,
                gender TEXT NOT NULL,
                specialization_id INTEGER NOT NULL,
                FOREIGN KEY (specialization_id) REFERENCES specializations(id)
            )
            """
        )

    def add(self, name: str, email: str, phone: str, birth: str, gender: str, specialization_id: int) -> int:
        # Insert a doctor record and return its id
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO doctors(name, email, phone, birth, gender, specialization_id)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (name, email, phone, birth, gender, specialization_id),
        )
        self.db.commit()
        return cursor.lastrowid

    def count_by_specialization_name(self, specialization_name: str) -> int:
        # Count doctors that belong to the provided specialization
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM doctors d
            JOIN specializations s ON s.id = d.specialization_id
            WHERE s.name = ?
            """,
            (specialization_name,),
        )
        (count,) = cursor.fetchone()
        return count
