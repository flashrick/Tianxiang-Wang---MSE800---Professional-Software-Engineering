from pathlib import Path
from database import Database
from courses import Courses
from students import Students
from lecturers import Lecturers
from course_lectures import CourseLectures


def needs_schema_reset(database: Database) -> bool:
    """Return True when the existing DB still uses an outdated schema."""

    cursor = database.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='courses'")
    if cursor.fetchone() is None:
        return False
    cursor.execute("PRAGMA table_info(courses)")
    columns = [row[1] for row in cursor.fetchall()]
    return "program_id" in columns


if __name__ == "__main__":
    db_file = Path("school.db")
    db_exists = db_file.exists()

    db = Database(str(db_file))

    if db_exists and needs_schema_reset(db):
        # Delete the legacy database so the new ER structure can be applied
        db.close()
        db_file.unlink()
        db_exists = False
        db = Database(str(db_file))

    courses = Courses(db)
    students = Students(db)
    lecturers = Lecturers(db)
    course_lectures = CourseLectures(db)

    if not db_exists:
        # Create all tables and insert the base information shown in the ERD
        courses.create_table()
        students.create_table()
        lecturers.create_table()
        course_lectures.create_table()
        db.commit()

        # Insert the two MSE courses
        mse800_id = courses.add(
            "Professional Software Engineering",
            "2025-11-17",
            "2026-03-01",
            "MSE800",
        )
        mse801_id = courses.add(
            "Research Methods",
            "2025-11-17",
            "2026-03-01",
            "MSE801",
        )

        # Add several students that are linked straight to MSE800
        students.add("Tom", "1999-07-14", "Male", mse800_id)
        students.add("Peter", "1998-05-02", "Male", mse800_id)
        students.add("Maya", "2000-01-23", "Female", mse800_id)

        # Assign lecturers to the MSE801 course
        nvidia_id = lecturers.add("Nvidia", "1983-10-04", "Female")
        amd_id = lecturers.add("AMD", "1988-06-21", "Male")
        course_lectures.add(mse801_id, nvidia_id)
        course_lectures.add(mse801_id, amd_id)

    # Show the number of students for the MSE800 course
    mse800_count = students.count_by_course_code("MSE800")
    print(f"Number of students taking MSE800: {mse800_count}")

    # Show the list of lecturer names for the MSE801 course
    teacher_names = course_lectures.get_teacher_names_by_course("MSE801")
    print("Teachers for MSE801:")
    for name in teacher_names:
        print(f" - {name}")

    db.close()
