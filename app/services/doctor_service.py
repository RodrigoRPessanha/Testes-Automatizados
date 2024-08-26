from app.repositories.doctor_repository import DoctorRepository
from app.entities.doctor import Doctor

class DoctorService:
    def __init__(self, repository: DoctorRepository):
        self.repository = repository

    def add_doctor(self, doctor: Doctor):
        if not doctor.name or not doctor.specialty:
            raise ValueError("Doctor must have a name and specialty")
        self.repository.add_doctor(doctor)

    def list_doctors(self):
        return self.repository.get_all_doctors()

    def get_doctor(self, doctor_id: int) -> Doctor:
        doctor = self.repository.get_doctor_by_id(doctor_id)
        if not doctor:
            raise ValueError("Doctor not found")
        return doctor
