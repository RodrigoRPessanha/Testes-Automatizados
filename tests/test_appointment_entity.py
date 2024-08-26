import pytest
from app.entities.appointment import Appointment
from datetime import datetime

def test_create_appointment():
    date = datetime.now()
    appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=date)
    assert appointment.id == 1
    assert appointment.doctor_id == 1
    assert appointment.patient_id == 1
    assert appointment.date == date

def test_create_appointment_invalid_data():
    with pytest.raises(ValueError):
        Appointment(id=1, doctor_id=0, patient_id=1, date=datetime.now())

    with pytest.raises(ValueError):
        Appointment(id=1, doctor_id=1, patient_id=0, date=datetime.now())

def test_appointment_str_representation():
    date = datetime.now()
    appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=date)
    assert str(appointment) == f"Appointment(id=1, doctor_id=1, patient_id=1, date={date})"

def test_update_appointment():
    date = datetime.now()
    appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=date)
    new_date = datetime.now()
    appointment.date = new_date
    assert appointment.date == new_date
