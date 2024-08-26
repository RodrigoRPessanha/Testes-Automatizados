from pydantic import BaseModel, Field

class Patient(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0)

    def __str__(self):
        return f"Patient(id={self.id}, name='{self.name}', age={self.age})"
