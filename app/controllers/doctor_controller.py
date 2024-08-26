from fastapi import APIRouter, HTTPException
from app.entities.doctor import Doctor
from app.services.doctor_service import DoctorService
from app.repositories.doctor_repository import DoctorRepository

router = APIRouter()

doctor_service = DoctorService(DoctorRepository())

@router.post("/doctors/")
def add_doctor(doctor: Doctor):
    try:
        doctor_service.add_doctor(doctor)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return doctor

@router.get("/doctors/")
def list_doctors():
    return doctor_service.list_doctors()

@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):
    try:
        return doctor_service.get_doctor(doctor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
