import pytest
from app.entities.patient import Patient

def test_create_patient():
    patient = Patient(id=1, name="John Doe", age=30)
    assert patient.id == 1
    assert patient.name == "John Doe"
    assert patient.age == 30

def test_create_patient_invalid_data():
    with pytest.raises(ValueError):
        Patient(id=1, name="", age=30)

    with pytest.raises(ValueError):
        Patient(id=1, name="John Doe", age=-5)

def test_patient_str_representation():
    patient = Patient(id=1, name="John Doe", age=30)
    assert str(patient) == "Patient(id=1, name='John Doe', age=30)"

def test_update_patient():
    patient = Patient(id=1, name="John Doe", age=30)
    patient.name = "Jane Doe"
    patient.age = 31
    assert patient.name == "Jane Doe"
    assert patient.age == 31
