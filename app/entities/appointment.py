from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Appointment(BaseModel):
    id: Optional[int] = None
    doctor_id: int = Field(..., gt=0)
    patient_id: int = Field(..., gt=0)
    date: datetime

    def __str__(self):
        return f"Appointment(id={self.id}, doctor_id={self.doctor_id}, patient_id={self.patient_id}, date={self.date})"