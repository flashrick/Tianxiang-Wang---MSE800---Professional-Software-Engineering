Activity 4 contains a small SQLite + Python project that illustrates how to read and write the Course / Student / Lecturer schema from the ER diagram in this folder. The code is kept intentionally compact for classroom use and every table has its own helper class so you can follow the OOP structure easily.

## Structure
- `database.py` wraps the SQLite connection so all helpers share the same cursor.
- `courses.py`, `students.py`, `lecturers.py`, `course_lectures.py` each represent one table with simple create/add/get methods.
- `main.py` orchestrates everything. When `school.db` does not exist it builds the schema, seeds two MSE courses, adds several students, and maps lecturers to MSE801. Future runs reuse the stored data and only run the two required queries:
  - Count students enrolled in course code `MSE800`.
  - List teachers who lecture course code `MSE801`.

## Table schema
- **courses**
  - `id INTEGER PRIMARY KEY`
  - `name TEXT NOT NULL`
  - `start_date TEXT NOT NULL`
  - `end_date TEXT NOT NULL`
  - `code TEXT NOT NULL UNIQUE`
- **students**
  - `id INTEGER PRIMARY KEY`
  - `name TEXT NOT NULL`
  - `birth_date TEXT NOT NULL`
  - `gender TEXT NOT NULL`
  - `course_id INTEGER NOT NULL` referencing `courses(id)`
- **lecturers**
  - `id INTEGER PRIMARY KEY`
  - `name TEXT NOT NULL`
  - `birth_date TEXT NOT NULL`
  - `gender TEXT NOT NULL`
- **course_lectures**
  - `course_id INTEGER NOT NULL` referencing `courses(id)`
  - `lecturer_id INTEGER NOT NULL` referencing `lecturers(id)`
  - Combined primary key `(course_id, lecturer_id)`

## Getting started
1. Open a shell in `week3/activity 4`.
2. (Optional) delete `school.db` if you need a fresh database.
3. Run `python3 main.py`.

The script will print the student count for `MSE800` and the lecturer names for `MSE801`. If you modify the ER diagram again, adjust the table helper classes first, delete `school.db`, and rerun `python3 main.py` to rebuild the database with the new structure.
