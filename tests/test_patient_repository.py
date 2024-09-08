import pytest
import sqlite3
from app.repositories.patient_repository import PatientRepository
from app.entities.patient import Patient

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    yield connection
    connection.close()

@pytest.fixture
def patient_repository(db_connection):
    return PatientRepository(db_path=":memory:")

def test_add_patient(patient_repository):
    patient = Patient(id=1, name="John Doe", age=30)

    patient_repository.add_patient(patient)
    assert len(patient_repository.get_all_patients()) == 1
    assert patient_repository.get_all_patients()[0] == patient

def test_get_all_patients(patient_repository):
    assert patient_repository.get_all_patients() == []

def test_get_patient_by_id(patient_repository):
    patient = Patient(id=1, name="John Doe", age=30)
    patient_repository.add_patient(patient)

    found_patient = patient_repository.get_patient_by_id(1)
    assert found_patient == patient

def test_get_patient_by_id_not_found(patient_repository):
    assert patient_repository.get_patient_by_id(999) is None

def test_close_connection(patient_repository):
    assert patient_repository.connection is not None

    patient_repository.close()

    with pytest.raises(sqlite3.ProgrammingError):
        patient_repository.connection.execute("SELECT 1")