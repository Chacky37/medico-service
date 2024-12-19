from pydantic import BaseModel

class MedicoSchema(BaseModel):
    id: int
    nombre: str
    especialidad: str

    class Config:
        orm_mode = True
