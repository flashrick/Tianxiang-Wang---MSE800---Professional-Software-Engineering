Activity 5 mirrors the Activity 4 project but uses the medical ER diagram in this folder. The code demonstrates how to model doctors, patients, and doctor specializations with SQLite and simple Python classes.

Author: Wade Wang  
Email: 270430358@yoobeestudent.ac.nz

## Structure
- `database.py` opens the SQLite connection and shares it across helpers.
- `doctors.py`, `patients.py`, `specializations.py` each implement one table from the ER diagram with create/add helpers plus the custom query helpers needed for this activity.
- `main.py` builds the schema when `clinic.db` is missing, seeds ten common-name patients (five older than 66) and three Ophthalmology doctors (stored with a direct foreign key), then:
  - Prints every senior patient (>65) with all stored fields.
  - Prints how many doctors have the Ophthalmology specialization.

## Table schema
- **doctors**
  - `id INTEGER PRIMARY KEY`
  - `name TEXT NOT NULL`
  - `email TEXT NOT NULL UNIQUE`
  - `phone TEXT NOT NULL`
  - `birth TEXT NOT NULL`
  - `gender TEXT NOT NULL`
- **patients**
  - `id INTEGER PRIMARY KEY`
  - `name TEXT NOT NULL`
  - `email TEXT NOT NULL UNIQUE`
  - `phone TEXT NOT NULL`
  - `birth TEXT NOT NULL`
  - `gender TEXT NOT NULL`
- **specializations**
  - `id INTEGER PRIMARY KEY`
  - `name TEXT NOT NULL UNIQUE`
- **doctors**
  - `id INTEGER PRIMARY KEY`
  - `name TEXT NOT NULL`
  - `email TEXT NOT NULL UNIQUE`
  - `phone TEXT NOT NULL`
  - `birth TEXT NOT NULL`
  - `gender TEXT NOT NULL`
  - `specialization_id INTEGER NOT NULL` references `specializations(id)`

## Getting started
1. Open a shell in `week3/activity 5`.
2. Delete `clinic.db` if you want to rebuild from scratch.
3. Run `python3 main.py`.

The script lists the senior patients and shows the number of Ophthalmology doctors. Update the table helpers and remove `clinic.db` if you change the ER diagram so the schema is recreated on the next run.
