import sqlite3
from typing import List
from app.entities.doctor import Doctor

class DoctorRepository:
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self.create_table()

    def create_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        with self.create_connection() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS doctors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialty TEXT NOT NULL
                )
            """)

    def add_doctor(self, doctor: Doctor):
        with self.create_connection() as connection:
            connection.execute(
                "INSERT INTO doctors (name, specialty) VALUES (?, ?)",
                (doctor.name, doctor.specialty)
            )

    def get_all_doctors(self) -> List[Doctor]:
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, specialty FROM doctors")
            rows = cursor.fetchall()
            return [Doctor(id=row[0], name=row[1], specialty=row[2]) for row in rows]

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        with self.create_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, name, specialty FROM doctors WHERE id = ?", (doctor_id,))
            row = cursor.fetchone()
            if row:
                return Doctor(id=row[0], name=row[1], specialty=row[2])
            return None