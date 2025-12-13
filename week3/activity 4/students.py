from database import Database


class Students:
    """Table helper that builds and fills the students table."""

    def __init__(self, db: Database) -> None:
        # Keep database connection ready for insert and query work
        self.db = db

    def create_table(self) -> None:
        # Create the students table with a link to courses
        self.db.cursor().execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birth_date TEXT NOT NULL,
                gender TEXT NOT NULL,
                course_id INTEGER NOT NULL,
                FOREIGN KEY (course_id) REFERENCES courses(id)
            )
            """
        )

    def add(self, name: str, birth_date: str, gender: str, course_id: int) -> int:
        # Insert one student record and return the id
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO students(name, birth_date, gender, course_id) VALUES (?, ?, ?, ?)",
            (name, birth_date, gender, course_id),
        )
        self.db.commit()
        return cursor.lastrowid

    def count_by_course_code(self, code: str) -> int:
        # Count how many students are enrolled in the matching course code
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM students s
            JOIN courses c ON s.course_id = c.id
            WHERE c.code = ?
            """,
            (code,),
        )
        (count,) = cursor.fetchone()
        return count
