import pytest
import sqlite3
from app.repositories.appointment_repository import AppointmentRepository
from app.entities.appointment import Appointment
from datetime import datetime

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    yield connection
    connection.close()

@pytest.fixture
def appointment_repository(db_connection):
    return AppointmentRepository(db_path=":memory:")

def test_add_appointment(appointment_repository):
    appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=datetime.now())

    appointment_repository.add_appointment(appointment)
    assert len(appointment_repository.get_all_appointments()) == 1
    assert appointment_repository.get_all_appointments()[0] == appointment

def test_get_all_appointments(appointment_repository):
    assert appointment_repository.get_all_appointments() == []

def test_get_appointment_by_id(appointment_repository):
    appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=datetime.now())
    appointment_repository.add_appointment(appointment)

    found_appointment = appointment_repository.get_appointment_by_id(1)
    assert found_appointment == appointment

def test_get_appointment_by_id_not_found(appointment_repository):
    assert appointment_repository.get_appointment_by_id(999) is None

def test_get_appointments_by_doctor_id(appointment_repository):
    appointment1 = Appointment(id=1, doctor_id=1, patient_id=1, date=datetime.now())
    appointment2 = Appointment(id=2, doctor_id=1, patient_id=2, date=datetime.now())
    appointment3 = Appointment(id=3, doctor_id=2, patient_id=1, date=datetime.now())
    appointment_repository.add_appointment(appointment1)
    appointment_repository.add_appointment(appointment2)
    appointment_repository.add_appointment(appointment3)

    found_appointments = appointment_repository.get_appointments_by_doctor_id(1)
    assert len(found_appointments) == 2
    assert appointment1 in found_appointments
    assert appointment2 in found_appointments
    assert appointment3 not in found_appointments

def test_get_appointments_by_patient_id(appointment_repository):
    appointment1 = Appointment(id=1, doctor_id=1, patient_id=1, date=datetime.now())
    appointment2 = Appointment(id=2, doctor_id=2, patient_id=1, date=datetime.now())
    appointment3 = Appointment(id=3, doctor_id=1, patient_id=2, date=datetime.now())
    appointment_repository.add_appointment(appointment1)
    appointment_repository.add_appointment(appointment2)
    appointment_repository.add_appointment(appointment3)

    found_appointments = appointment_repository.get_appointments_by_patient_id(1)
    assert len(found_appointments) == 2
    assert appointment1 in found_appointments
    assert appointment2 in found_appointments
    assert appointment3 not in found_appointments

def test_close_connection(appointment_repository):
    assert appointment_repository.connection is not None

    appointment_repository.close()

    with pytest.raises(sqlite3.ProgrammingError):
        appointment_repository.connection.execute("SELECT 1")
