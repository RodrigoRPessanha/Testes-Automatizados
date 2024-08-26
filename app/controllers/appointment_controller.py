from fastapi import APIRouter, HTTPException
from app.entities.appointment import Appointment
from app.services.appointment_service import AppointmentService
from app.repositories.appointment_repository import AppointmentRepository

router = APIRouter()

appointment_service = AppointmentService(AppointmentRepository())

@router.post("/appointments/")
def add_appointment(appointment: Appointment):
    try:
        appointment_service.add_appointment(appointment)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return appointment

@router.get("/appointments/")
def list_appointments():
    return appointment_service.list_appointments()

@router.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int):
    try:
        return appointment_service.get_appointment(appointment_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
