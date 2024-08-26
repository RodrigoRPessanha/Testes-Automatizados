import pytest
from unittest.mock import Mock
from fastapi.testclient import TestClient
from app.main import app
from app.repositories.appointment_repository import AppointmentRepository
from app.services.appointment_service import AppointmentService
from app.entities.appointment import Appointment
from datetime import datetime

client = TestClient(app)

def test_add_appointment_successful(monkeypatch):
    mock_service = Mock(AppointmentService)
    monkeypatch.setattr("app.controllers.appointment_controller.appointment_service", mock_service)

    response = client.post("/appointments/", json={"id": 1, "doctor_id": 1, "patient_id": 1, "date": datetime.now().isoformat()})
    assert response.status_code == 200
    assert response.json()["doctor_id"] == 1
    assert response.json()["patient_id"] == 1

    mock_service.add_appointment.assert_called_once()

def test_add_appointment_invalid_data(monkeypatch):
    repository_mock = Mock(AppointmentRepository)
    service = AppointmentService(repository_mock)

    # Não precisa simular erro aqui, porque o erro virá da validação do Pydantic
    response = client.post("/appointments/", json={"id": 1, "doctor_id": 0, "patient_id": 1, "date": None})

    assert response.status_code == 422  # Unprocessable Entity
    assert "detail" in response.json()
    assert isinstance(response.json()["detail"], list)
    assert len(response.json()["detail"]) > 0


def test_list_appointments(monkeypatch):
    mock_service = Mock(AppointmentService)
    monkeypatch.setattr("app.controllers.appointment_controller.appointment_service", mock_service)

    mock_service.list_appointments.return_value = []
    response = client.get("/appointments/")
    
    assert response.status_code == 200
    assert response.json() == []

    mock_service.list_appointments.assert_called_once()

def test_get_appointment_by_id_successful(monkeypatch):
    mock_service = Mock(AppointmentService)
    monkeypatch.setattr("app.controllers.appointment_controller.appointment_service", mock_service)

    appointment = Appointment(id=1, doctor_id=1, patient_id=1, date=datetime.now())
    mock_service.get_appointment.return_value = appointment

    response = client.get("/appointments/1")
    assert response.status_code == 200
    assert response.json()["doctor_id"] == 1
    assert response.json()["patient_id"] == 1

    mock_service.get_appointment.assert_called_once_with(1)

def test_get_appointment_by_id_not_found(monkeypatch):
    mock_service = Mock(AppointmentService)
    monkeypatch.setattr("app.controllers.appointment_controller.appointment_service", mock_service)

    mock_service.get_appointment.side_effect = ValueError("Appointment not found")

    response = client.get("/appointments/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Appointment not found"}

def test_add_appointment_service_error(monkeypatch):
    mock_service = Mock(AppointmentService)
    monkeypatch.setattr("app.controllers.appointment_controller.appointment_service", mock_service)

    mock_service.add_appointment.side_effect = ValueError("Service error")
    response = client.post("/appointments/", json={"id": 1, "doctor_id": 1, "patient_id": 1, "date": datetime.now().isoformat()})

    assert response.status_code == 400
    assert response.json() == {"detail": "Service error"}
