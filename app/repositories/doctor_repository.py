import sqlite3
from typing import List
from app.entities.doctor import Doctor

class DoctorRepository:
    def __init__(self, db_path: str = "database.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS doctors (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    specialty TEXT NOT NULL
                )
            """)

    def add_doctor(self, doctor: Doctor):
        with self.connection:
            self.connection.execute(
                "INSERT INTO doctors (id, name, specialty) VALUES (?, ?, ?)",
                (doctor.id, doctor.name, doctor.specialty)
            )

    def get_all_doctors(self) -> List[Doctor]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, specialty FROM doctors")
        rows = cursor.fetchall()
        return [Doctor(id=row[0], name=row[1], specialty=row[2]) for row in rows]

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, specialty FROM doctors WHERE id = ?", (doctor_id,))
        row = cursor.fetchone()
        if row:
            return Doctor(id=row[0], name=row[1], specialty=row[2])
        return None

    def close(self):
        self.connection.close()
