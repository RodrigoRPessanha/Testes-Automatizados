from app.repositories.appointment_repository import AppointmentRepository
from app.entities.appointment import Appointment

class AppointmentService:
    def __init__(self, repository: AppointmentRepository):
        self.repository = repository

    def add_appointment(self, appointment: Appointment):
        if not appointment.doctor_id or not appointment.patient_id or not appointment.date:
            raise ValueError("Appointment must have doctor_id, patient_id and date")
        self.repository.add_appointment(appointment)

    def list_appointments(self):
        return self.repository.get_all_appointments()

    def get_appointment(self, appointment_id: int) -> Appointment:
        appointment = self.repository.get_appointment_by_id(appointment_id)
        if not appointment:
            raise ValueError("Appointment not found")
        return appointment
