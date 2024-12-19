from pydantic import BaseModel

class Medico(BaseModel):
    id: int
    nombre: str
    especialidad: str
