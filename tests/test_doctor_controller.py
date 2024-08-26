import pytest
from unittest.mock import Mock
from fastapi.testclient import TestClient
from app.main import app
from app.services.doctor_service import DoctorService
from app.entities.doctor import Doctor

client = TestClient(app)

def test_add_doctor_successful(monkeypatch):
    mock_service = Mock(DoctorService)
    monkeypatch.setattr("app.controllers.doctor_controller.doctor_service", mock_service)

    response = client.post("/doctors/", json={"id": 1, "name": "Dr. Smith", "specialty": "Cardiology"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Dr. Smith", "specialty": "Cardiology"}

    mock_service.add_doctor.assert_called_once()

def test_add_doctor_invalid_data(monkeypatch):
    mock_service = Mock(DoctorService)
    monkeypatch.setattr("app.controllers.doctor_controller.doctor_service", mock_service)

    response = client.post("/doctors/", json={"id": 1, "name": "", "specialty": ""})

    assert response.status_code == 422  # 422 Unprocessable Entity
    assert "detail" in response.json()
    assert isinstance(response.json()["detail"], list)
    assert len(response.json()["detail"]) > 0


def test_list_doctors(monkeypatch):
    mock_service = Mock(DoctorService)
    monkeypatch.setattr("app.controllers.doctor_controller.doctor_service", mock_service)

    mock_service.list_doctors.return_value = []
    response = client.get("/doctors/")
    
    assert response.status_code == 200
    assert response.json() == []

    mock_service.list_doctors.assert_called_once()

def test_get_doctor_by_id_successful(monkeypatch):
    mock_service = Mock(DoctorService)
    monkeypatch.setattr("app.controllers.doctor_controller.doctor_service", mock_service)

    doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")
    mock_service.get_doctor.return_value = doctor

    response = client.get("/doctors/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Dr. Smith", "specialty": "Cardiology"}

    mock_service.get_doctor.assert_called_once_with(1)

def test_get_doctor_by_id_not_found(monkeypatch):
    mock_service = Mock(DoctorService)
    monkeypatch.setattr("app.controllers.doctor_controller.doctor_service", mock_service)

    mock_service.get_doctor.side_effect = ValueError("Doctor not found")

    response = client.get("/doctors/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Doctor not found"}

def test_add_doctor_service_error(monkeypatch):
    mock_service = Mock(DoctorService)
    monkeypatch.setattr("app.controllers.doctor_controller.doctor_service", mock_service)

    mock_service.add_doctor.side_effect = ValueError("Service error")
    response = client.post("/doctors/", json={"id": 1, "name": "Dr. Smith", "specialty": "Cardiology"})

    assert response.status_code == 400
    assert response.json() == {"detail": "Service error"}
