from app.repositories.patient_repository import PatientRepository
from app.entities.patient import Patient

class PatientService:
    def __init__(self, repository: PatientRepository):
        self.repository = repository

    def add_patient(self, patient: Patient):
        if not patient.name or patient.age <= 0:
            raise ValueError("Patient must have a name and valid age")
        self.repository.add_patient(patient)

    def list_patients(self):
        return self.repository.get_all_patients()

    def get_patient(self, patient_id: int) -> Patient:
        patient = self.repository.get_patient_by_id(patient_id)
        if not patient:
            raise ValueError("Patient not found")
        return patient
