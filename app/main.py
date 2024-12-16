from fastapi import FastAPI, HTTPException
from app.models import Medico
from app.schemas import MedicoSchema

app = FastAPI()

# Simulamos una base de datos en memoria
medicos_db = []

@app.get("/medicos", response_model=list[MedicoSchema])
def listar_medicos():
    return medicos_db

@app.post("/medicos", response_model=MedicoSchema)
def crear_medico(medico: MedicoSchema):
    nuevo_medico = Medico(**medico.dict())
    medicos_db.append(nuevo_medico)
    return nuevo_medico

@app.get("/medicos/{id}", response_model=MedicoSchema)
def obtener_medico(id: int):
    for medico in medicos_db:
        if medico.id == id:
            return medico
    raise HTTPException(status_code=404, detail="Médico no encontrado")

@app.post("/medicos/llenar")
def llenar_medicos():
    medicos_por_defecto = [
        {"id": 1, "nombre": "Dr. Juan Pérez", "especialidad": "Cardiología"},
        {"id": 2, "nombre": "Dra. Ana López", "especialidad": "Pediatría"},
        {"id": 3, "nombre": "Dr. Luis García", "especialidad": "Neurología"},
    ]
    for medico_data in medicos_por_defecto:
        nuevo_medico = Medico(**medico_data)
        medicos_db.append(nuevo_medico)
    return {"mensaje": "Datos de médicos añadidos correctamente"}
