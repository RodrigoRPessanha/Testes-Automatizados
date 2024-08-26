import pytest
import sqlite3
from app.repositories.doctor_repository import DoctorRepository
from app.entities.doctor import Doctor

@pytest.fixture
def db_connection():
    # Cria uma conexão com o banco de dados em memória
    connection = sqlite3.connect(":memory:")
    yield connection
    connection.close()

@pytest.fixture
def doctor_repository(db_connection):
    # Usa a conexão com o banco de dados em memória para criar o repositório
    return DoctorRepository(db_path=":memory:")

def test_add_doctor(doctor_repository):
    doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")

    doctor_repository.add_doctor(doctor)
    assert len(doctor_repository.get_all_doctors()) == 1
    assert doctor_repository.get_all_doctors()[0] == doctor

def test_get_all_doctors(doctor_repository):
    assert doctor_repository.get_all_doctors() == []

def test_get_doctor_by_id(doctor_repository):
    doctor = Doctor(id=1, name="Dr. Smith", specialty="Cardiology")
    doctor_repository.add_doctor(doctor)

    found_doctor = doctor_repository.get_doctor_by_id(1)
    assert found_doctor == doctor

def test_get_doctor_by_id_not_found(doctor_repository):
    assert doctor_repository.get_doctor_by_id(999) is None

def test_close_connection(doctor_repository):
    # Garanta que a conexão está aberta antes de fechar
    assert doctor_repository.connection is not None

    # Fechar a conexão
    doctor_repository.close()

    # Tentar usar a conexão depois de fechá-la deve gerar um erro
    with pytest.raises(sqlite3.ProgrammingError):
        doctor_repository.connection.execute("SELECT 1")
