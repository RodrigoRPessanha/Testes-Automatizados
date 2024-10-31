import sqlite3
from typing import List
from app.entities.patient import Patient

class PatientRepository:
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self.create_table()

    def create_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self.create_connection() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            """)

    def add_patient(self, patient: Patient):
        with self.create_connection() as connection:
            connection.execute(
                "INSERT INTO patients (name, age) VALUES (?, ?)",
                (patient.name, patient.age)
            )

    def get_all_patients(self) -> List[Patient]:
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, age FROM patients")
            rows = cursor.fetchall()
            return [Patient(id=row[0], name=row[1], age=row[2]) for row in rows]

    def get_patient_by_id(self, patient_id: int) -> Patient:
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, age FROM patients WHERE id = ?", (patient_id,))
            row = cursor.fetchone()
            if row:
                return Patient(id=row[0], name=row[1], age=row[2])
            return None