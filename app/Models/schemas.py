from pydantic import BaseModel

class MedicoSchema(BaseModel):
    id: int
    nombre: str
    especialidad: str
    