from fastapi import FastAPI
from app.controllers import doctor_controller, patient_controller, appointment_controller
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Substitua pelo domínio do seu frontend, se necessário
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

app.include_router(doctor_controller.router)
app.include_router(patient_controller.router)
app.include_router(appointment_controller.router)

# Rodar usando o comando:   uvicorn app.main:app --reload