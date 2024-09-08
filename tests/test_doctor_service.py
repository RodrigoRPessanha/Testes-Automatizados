import pytest
from unittest.mock import Mock
from app.repositories.doctor_repository import DoctorRepository
from app.services.doctor_service import DoctorService
from app.entities.doctor import Doctor

def test_add_doctor():
    repository_mock = Mock()
    service = DoctorService(repository_mock)

    doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")
    service.add_doctor(doctor)

    repository_mock.add_doctor.assert_called_once_with(doctor)

def test_add_doctor_with_invalid_data():
    repository_mock = Mock()
    service = DoctorService(repository_mock)

    with pytest.raises(ValueError):
        service.add_doctor(Doctor(id=1, name="", specialty=""))

def test_list_doctors():
    repository_mock = Mock()
    service = DoctorService(repository_mock)

    service.list_doctors()

    repository_mock.get_all_doctors.assert_called_once()

def test_get_doctor_by_id():
    repository_mock = Mock()
    service = DoctorService(repository_mock)

    doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")
    repository_mock.get_doctor_by_id.return_value = doctor

    result = service.get_doctor(1)

    assert result == doctor
    repository_mock.get_doctor_by_id.assert_called_once_with(1)
    
def test_get_doctor_by_id_not_found():
    repository_mock = Mock()
    service = DoctorService(repository_mock)

    repository_mock.get_doctor_by_id.return_value = None

    with pytest.raises(ValueError):
        service.get_doctor(1)


def test_add_doctor_invalid_name(monkeypatch):
    repository_mock = Mock(DoctorRepository)
    service = DoctorService(repository_mock)

    invalid_doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")
    invalid_doctor.name = ""  
    
    with pytest.raises(ValueError) as excinfo:
        service.add_doctor(invalid_doctor)
    assert str(excinfo.value) == "Doctor must have a name and specialty"

def test_add_doctor_invalid_specialty(monkeypatch):
    repository_mock = Mock(DoctorRepository)
    service = DoctorService(repository_mock)

    invalid_doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")
    invalid_doctor.specialty = ""
    
    with pytest.raises(ValueError) as excinfo:
        service.add_doctor(invalid_doctor)
    assert str(excinfo.value) == "Doctor must have a name and specialty"
