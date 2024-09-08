import pytest
from unittest.mock import Mock
from app.entities.patient import Patient
from app.repositories.appointment_repository import AppointmentRepository
from app.repositories.patient_repository import PatientRepository
from app.services.appointment_service import AppointmentService
from app.entities.appointment import Appointment
from datetime import datetime

from app.services.patient_service import PatientService

def test_add_appointment():
    repository_mock = Mock()
    service = AppointmentService(repository_mock)

    appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=datetime.now())
    service.add_appointment(appointment)

    repository_mock.add_appointment.assert_called_once_with(appointment)

def test_add_appointment_with_invalid_data():
    repository_mock = Mock()
    service = AppointmentService(repository_mock)

    with pytest.raises(ValueError):
        service.add_appointment(Appointment(id=1, doctor_id=0, patient_id=0, date=None))

def test_list_appointments():
    repository_mock = Mock()
    service = AppointmentService(repository_mock)

    service.list_appointments()

    repository_mock.get_all_appointments.assert_called_once()

def test_get_appointment_by_id():
    repository_mock = Mock()
    service = AppointmentService(repository_mock)

    appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=datetime.now())
    repository_mock.get_appointment_by_id.return_value = appointment

    result = service.get_appointment(1)

    assert result == appointment
    repository_mock.get_appointment_by_id.assert_called_once_with(1)
    
def test_get_appointment_by_id_not_found():
    repository_mock = Mock()
    service = AppointmentService(repository_mock)

    repository_mock.get_appointment_by_id.return_value = None

    with pytest.raises(ValueError):
        service.get_appointment(1)

def test_add_appointment_missing_doctor_id(monkeypatch):
    repository_mock = Mock(AppointmentRepository)
    service = AppointmentService(repository_mock)

    invalid_appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=datetime.now())
    invalid_appointment.doctor_id = None
    
    with pytest.raises(ValueError) as excinfo:
        service.add_appointment(invalid_appointment)
    assert str(excinfo.value) == "Appointment must have doctor_id, patient_id and date"

def test_add_appointment_missing_patient_id(monkeypatch):
    repository_mock = Mock(AppointmentRepository)
    service = AppointmentService(repository_mock)

    invalid_appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=datetime.now())
    invalid_appointment.patient_id = None
    
    with pytest.raises(ValueError) as excinfo:
        service.add_appointment(invalid_appointment)
    assert str(excinfo.value) == "Appointment must have doctor_id, patient_id and date"

def test_add_patient_invalid_name(monkeypatch):
    repository_mock = Mock(PatientRepository)
    service = PatientService(repository_mock)

    invalid_patient = Patient(id=1, name="John Doe", age=30)
    invalid_patient.name = "" 
    
    with pytest.raises(ValueError) as excinfo:
        service.add_patient(invalid_patient)
    assert str(excinfo.value) == "Patient must have a name and valid age"

def test_add_patient_invalid_age(monkeypatch):
    repository_mock = Mock(PatientRepository)
    service = PatientService(repository_mock)

    invalid_patient = Patient(id=1, name="John Doe", age=30)
    invalid_patient.age = -1 
    
    with pytest.raises(ValueError) as excinfo:
        service.add_patient(invalid_patient)
    assert str(excinfo.value) == "Patient must have a name and valid age"

