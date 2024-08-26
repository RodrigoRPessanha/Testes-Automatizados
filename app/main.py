from fastapi import FastAPI
from app.controllers import doctor_controller, patient_controller, appointment_controller

app = FastAPI()

app.include_router(doctor_controller.router)
app.include_router(patient_controller.router)
app.include_router(appointment_controller.router)

# Rodar usando o comando:   uvicorn app.main:app --reload