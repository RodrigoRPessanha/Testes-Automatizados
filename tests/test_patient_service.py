import pytest
from unittest.mock import Mock
from app.services.patient_service import PatientService
from app.entities.patient import Patient

def test_add_patient():
    repository_mock = Mock()
    service = PatientService(repository_mock)

    patient = Patient(id=1, name="John Doe", age=30)
    service.add_patient(patient)

    repository_mock.add_patient.assert_called_once_with(patient)

def test_add_patient_with_invalid_data():
    repository_mock = Mock()
    service = PatientService(repository_mock)

    with pytest.raises(ValueError):
        service.add_patient(Patient(id=1, name="", age=-1))

def test_list_patients():
    repository_mock = Mock()
    service = PatientService(repository_mock)

    service.list_patients()

    repository_mock.get_all_patients.assert_called_once()

def test_get_patient_by_id():
    repository_mock = Mock()
    service = PatientService(repository_mock)

    patient = Patient(id=1, name="John Doe", age=30)
    repository_mock.get_patient_by_id.return_value = patient

    result = service.get_patient(1)

    assert result == patient
    repository_mock.get_patient_by_id.assert_called_once_with(1)
    
def test_get_patient_by_id_not_found():
    repository_mock = Mock()
    service = PatientService(repository_mock)

    repository_mock.get_patient_by_id.return_value = None

    with pytest.raises(ValueError):
        service.get_patient(1)
