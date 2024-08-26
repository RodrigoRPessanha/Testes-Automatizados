from fastapi import APIRouter, HTTPException
from app.entities.patient import Patient
from app.services.patient_service import PatientService
from app.repositories.patient_repository import PatientRepository

router = APIRouter()

patient_service = PatientService(PatientRepository())

@router.post("/patients/")
def add_patient(patient: Patient):
    try:
        patient_service.add_patient(patient)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return patient

@router.get("/patients/")
def list_patients():
    return patient_service.list_patients()

@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    try:
        return patient_service.get_patient(patient_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
