from pydantic import BaseModel
#Es un validador de estructuras (diccionario)
class MedicoSchema(BaseModel):
    id: int
    nombre: str
    especialidad: str
    