import pytest
from app.entities.doctor import Doctor

def test_create_doctor():
    doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")
    assert doctor.id == 1
    assert doctor.name == "Dr. Smith"
    assert doctor.specialty == "Cardiology"

def test_create_doctor_invalid_data():
    with pytest.raises(ValueError):
        Doctor(id=1, name="", specialty="Cardiology")

    with pytest.raises(ValueError):
        Doctor(id=1, name="Dr. Smith", specialty="")

def test_doctor_str_representation():
    doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")
    assert str(doctor) == "Doctor(id=1, name='Dr. Smith', specialty='Cardiology')"

def test_update_doctor():
    doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")
    doctor.name = "Dr. John Smith"
    doctor.specialty = "Neurology"
    assert doctor.name == "Dr. John Smith"
    assert doctor.specialty == "Neurology"
