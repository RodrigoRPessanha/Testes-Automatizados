import pytest
import sqlite3
from app.repositories.patient_repository import PatientRepository
from app.entities.patient import Patient

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)
    connection.commit()
    yield connection
    connection.close()

@pytest.fixture
def patient_repo(db_connection):
    repo = PatientRepository(db_path=":memory:")
    repo.create_connection = lambda: db_connection
    return repo

def test_add_patient(patient_repo):
    patient = Patient(name="John Doe", age=30)
    patient_repo.add_patient(patient)
    patients = patient_repo.get_all_patients()
    assert len(patients) == 1

def test_get_all_patients(patient_repo):
    patient = Patient(name="John Doe", age=30)
    patient_repo.add_patient(patient)
    patients = patient_repo.get_all_patients()
    assert len(patients) == 1

def test_get_patient_by_id(patient_repo):
    patient = Patient(name="John Doe", age=30)
    patient_repo.add_patient(patient)
    fetched_patient = patient_repo.get_patient_by_id(1)
    assert fetched_patient is not None

def test_get_patient_by_id_not_found(patient_repo):
    fetched_patient = patient_repo.get_patient_by_id(1)
    assert fetched_patient is None