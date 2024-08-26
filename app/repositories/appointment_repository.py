import sqlite3
from typing import List
from app.entities.appointment import Appointment

class AppointmentRepository:
    def __init__(self, db_path: str = "database.db"):
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY,
                    doctor_id INTEGER NOT NULL,
                    patient_id INTEGER NOT NULL,
                    date TEXT NOT NULL
                )
            """)

    def add_appointment(self, appointment: Appointment):
        with self.connection:
            self.connection.execute(
                "INSERT INTO appointments (id, doctor_id, patient_id, date) VALUES (?, ?, ?, ?)",
                (appointment.id, appointment.doctor_id, appointment.patient_id, appointment.date.isoformat())
            )

    def get_all_appointments(self) -> List[Appointment]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, doctor_id, patient_id, date FROM appointments")
        rows = cursor.fetchall()
        return [Appointment(id=row[0], doctor_id=row[1], patient_id=row[2], date=row[3]) for row in rows]

    def get_appointment_by_id(self, appointment_id: int) -> Appointment:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, doctor_id, patient_id, date FROM appointments WHERE id = ?", (appointment_id,))
        row = cursor.fetchone()
        if row:
            return Appointment(id=row[0], doctor_id=row[1], patient_id=row[2], date=row[3])
        return None

    def get_appointments_by_doctor_id(self, doctor_id: int) -> List[Appointment]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, doctor_id, patient_id, date FROM appointments WHERE doctor_id = ?", (doctor_id,))
        rows = cursor.fetchall()
        return [Appointment(id=row[0], doctor_id=row[1], patient_id=row[2], date=row[3]) for row in rows]

    def get_appointments_by_patient_id(self, patient_id: int) -> List[Appointment]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, doctor_id, patient_id, date FROM appointments WHERE patient_id = ?", (patient_id,))
        rows = cursor.fetchall()
        return [Appointment(id=row[0], doctor_id=row[1], patient_id=row[2], date=row[3]) for row in rows]

    def close(self):
        self.connection.close()
