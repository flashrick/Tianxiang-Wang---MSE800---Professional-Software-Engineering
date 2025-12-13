from pathlib import Path
from database import Database
from doctors import Doctors
from patients import Patients
from specializations import Specializations


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    db_path = script_dir / "clinic.db"
    # Only build schema and seed data if the DB is missing
    db_exists = db_path.exists()

    db = Database(str(db_path))
    doctors = Doctors(db)
    patients = Patients(db)
    specializations = Specializations(db)

    if not db_exists:
        # Create the tables described by the ER diagram
        doctors.create_table()
        patients.create_table()
        specializations.create_table()
        db.commit()

        # Seed the new Ophthalmology specialization
        oph_id = specializations.add("Ophthalmology")

        # Seed doctors who all practice ophthalmology
        doctor_data = [
            (
                "Dr. Ethan Lee",
                "ethan.lee@example.com",
                "02020110120",
                "1972-06-14",
                "Male",
                oph_id,
            ),
            (
                "Dr. Grace Patel",
                "grace.patel@example.com",
                "02020130230",
                "1981-09-02",
                "Female",
                oph_id,
            ),
            (
                "Dr. Noah Bennett",
                "noah.bennett@example.com",
                "02020150340",
                "1978-12-29",
                "Male",
                oph_id,
            ),
        ]
        for doctor in doctor_data:
            doctors.add(*doctor)

        # Seed ten patients with common names, five of them older than 66
        patient_data = [
            ("John Smith", "john.smith@example.com", "02020111221", "1950-04-12", "Male"),
            ("Mary Johnson", "mary.johnson@example.com", "02020112232", "1948-09-03", "Female"),
            ("Robert Brown", "robert.brown@example.com", "02020113243", "1955-01-25", "Male"),
            ("Linda Davis", "linda.davis@example.com", "02020114254", "1945-07-16", "Female"),
            ("William Miller", "william.miller@example.com", "02020115265", "1953-02-08", "Male"),
            ("Emily Wilson", "emily.wilson@example.com", "02020116276", "1992-05-04", "Female"),
            ("David Moore", "david.moore@example.com", "02020117287", "1987-07-19", "Male"),
            ("Sophia Taylor", "sophia.taylor@example.com", "02020118298", "1995-11-30", "Female"),
            ("James Anderson", "james.anderson@example.com", "02020119309", "1980-03-22", "Male"),
            ("Olivia Thomas", "olivia.thomas@example.com", "02020120310", "1998-08-11", "Female"),
        ]
        for patient in patient_data:
            patients.add(*patient)

    # Show senior patients with all their details
    seniors = patients.get_seniors()
    print("Senior patients (>65 years old):")
    if not seniors:
        print(" - None")
    else:
        for senior in seniors:
            print(
                f" - ID: {senior[0]}, Name: {senior[1]}, Email: {senior[2]}, Phone: {senior[3]}, Birth: {senior[4]}, Gender: {senior[5]}"
            )

    # Show how many doctors cover the Ophthalmology specialization
    oph_count = doctors.count_by_specialization_name("Ophthalmology")
    print(f"Number of Ophthalmology doctors: {oph_count}")

    db.close()
