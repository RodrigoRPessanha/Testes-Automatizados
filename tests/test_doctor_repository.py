import pytest
import sqlite3
from app.repositories.doctor_repository import DoctorRepository
from app.entities.doctor import Doctor

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialty TEXT NOT NULL
        )
    """)
    connection.commit()
    yield connection
    connection.close()

@pytest.fixture
def doctor_repo(db_connection):
    repo = DoctorRepository(db_path=":memory:")
    repo.create_connection = lambda: db_connection
    return repo

def test_add_doctor(doctor_repo):
    doctor = Doctor(name="Dr. Smith", specialty="Cardiology")
    doctor_repo.add_doctor(doctor)
    doctors = doctor_repo.get_all_doctors()
    assert len(doctors) == 1

def test_get_all_doctors(doctor_repo):
    doctor = Doctor(name="Dr. Smith", specialty="Cardiology")
    doctor_repo.add_doctor(doctor)
    doctors = doctor_repo.get_all_doctors()
    assert len(doctors) == 1

def test_get_doctor_by_id(doctor_repo):
    doctor = Doctor(name="Dr. Smith", specialty="Cardiology")
    doctor_repo.add_doctor(doctor)
    fetched_doctor = doctor_repo.get_doctor_by_id(1)
    assert fetched_doctor is not None

def test_get_doctor_by_id_not_found(doctor_repo):
    fetched_doctor = doctor_repo.get_doctor_by_id(1)
    assert fetched_doctor is None