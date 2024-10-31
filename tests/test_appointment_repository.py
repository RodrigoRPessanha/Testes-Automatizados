import pytest
import sqlite3
from app.repositories.appointment_repository import AppointmentRepository
from app.entities.appointment import Appointment
from datetime import datetime

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_id INTEGER NOT NULL,
            patient_id INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    """)
    connection.commit()
    yield connection
    connection.close()

@pytest.fixture
def appointment_repo(db_connection):
    repo = AppointmentRepository(db_path=":memory:")
    repo.create_connection = lambda: db_connection
    return repo

def test_add_appointment(appointment_repo):
    appointment = Appointment(doctor_id=1, patient_id=1, date=datetime.now())
    appointment_repo.add_appointment(appointment)
    appointments = appointment_repo.get_all_appointments()
    assert len(appointments) == 1

def test_get_all_appointments(appointment_repo):
    appointment = Appointment(doctor_id=1, patient_id=1, date=datetime.now())
    appointment_repo.add_appointment(appointment)
    appointments = appointment_repo.get_all_appointments()
    assert len(appointments) == 1

def test_get_appointment_by_id(appointment_repo):
    appointment = Appointment(doctor_id=1, patient_id=1, date=datetime.now())
    appointment_repo.add_appointment(appointment)
    fetched_appointment = appointment_repo.get_appointment_by_id(1)
    assert fetched_appointment is not None

def test_get_appointment_by_id_not_found(appointment_repo):
    fetched_appointment = appointment_repo.get_appointment_by_id(1)
    assert fetched_appointment is None

def test_get_appointments_by_doctor_id(appointment_repo):
    appointment = Appointment(doctor_id=1, patient_id=1, date=datetime.now())
    appointment_repo.add_appointment(appointment)
    appointments = appointment_repo.get_appointments_by_doctor_id(1)
    assert len(appointments) == 1

def test_get_appointments_by_patient_id(appointment_repo):
    appointment = Appointment(doctor_id=1, patient_id=1, date=datetime.now())
    appointment_repo.add_appointment(appointment)
    appointments = appointment_repo.get_appointments_by_patient_id(1)
    assert len(appointments) == 1