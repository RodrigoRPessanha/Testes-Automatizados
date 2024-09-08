import pytest
from unittest.mock import Mock
from fastapi.testclient import TestClient
from app.main import app
from app.services.patient_service import PatientService
from app.entities.patient import Patient

client = TestClient(app)

def test_add_patient_successful(monkeypatch):
    mock_service = Mock(PatientService)
    monkeypatch.setattr("app.controllers.patient_controller.patient_service", mock_service)

    response = client.post("/patients/", json={"id": 1, "name": "John Doe", "age": 30})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "age": 30}

    mock_service.add_patient.assert_called_once()

def test_add_patient_invalid_data(monkeypatch):
    mock_service = Mock(PatientService)
    monkeypatch.setattr("app.controllers.patient_controller.patient_service", mock_service)

    response = client.post("/patients/", json={"id": 1, "name": "", "age": -1})

    assert response.status_code == 422
    assert "detail" in response.json()
    assert isinstance(response.json()["detail"], list)
    assert len(response.json()["detail"]) > 0


def test_list_patients(monkeypatch):
    mock_service = Mock(PatientService)
    monkeypatch.setattr("app.controllers.patient_controller.patient_service", mock_service)

    mock_service.list_patients.return_value = []
    response = client.get("/patients/")
    
    assert response.status_code == 200
    assert response.json() == []

    mock_service.list_patients.assert_called_once()

def test_get_patient_by_id_successful(monkeypatch):
    mock_service = Mock(PatientService)
    monkeypatch.setattr("app.controllers.patient_controller.patient_service", mock_service)

    patient = Patient(id=1, name="John Doe", age=30)
    mock_service.get_patient.return_value = patient

    response = client.get("/patients/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "age": 30}

    mock_service.get_patient.assert_called_once_with(1)

def test_get_patient_by_id_not_found(monkeypatch):
    mock_service = Mock(PatientService)
    monkeypatch.setattr("app.controllers.patient_controller.patient_service", mock_service)

    mock_service.get_patient.side_effect = ValueError("Patient not found")

    response = client.get("/patients/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Patient not found"}

def test_add_patient_service_error(monkeypatch):
    mock_service = Mock(PatientService)
    monkeypatch.setattr("app.controllers.patient_controller.patient_service", mock_service)

    mock_service.add_patient.side_effect = ValueError("Service error")
    response = client.post("/patients/", json={"id": 1, "name": "John Doe", "age": 30})

    assert response.status_code == 400
    assert response.json() == {"detail": "Service error"}
