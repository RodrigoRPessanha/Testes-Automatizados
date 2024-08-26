import sqlite3
from app.entities.patient import Patient

class PatientRepository:
    def __init__(self, db_path: str = "database.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            """)

    def add_patient(self, patient: Patient):
        with self.connection:
            self.connection.execute(
                "INSERT INTO patients (id, name, age) VALUES (?, ?, ?)",
                (patient.id, patient.name, patient.age)
            )

    def get_all_patients(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, age FROM patients")
        rows = cursor.fetchall()
        return [Patient(id=row[0], name=row[1], age=row[2]) for row in rows]

    def get_patient_by_id(self, patient_id: int) -> Patient:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, age FROM patients WHERE id = ?", (patient_id,))
        row = cursor.fetchone()
        if row:
            return Patient(id=row[0], name=row[1], age=row[2])
        return None

    def close(self):
        self.connection.close()