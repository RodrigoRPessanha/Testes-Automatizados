from typing import Optional
from pydantic import BaseModel, Field

class Doctor(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1)
    specialty: str = Field(..., min_length=1)

    def __str__(self):
        return f"Doctor(id={self.id}, name='{self.name}', specialty='{self.specialty}')"
