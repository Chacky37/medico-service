from fastapi import FastAPI, HTTPException
from app.Controllers.Crear_Usuario import Crear_Medicos
from app.Models.models import Medico
from app.Models.schemas import MedicoSchema
from app.Controllers.obtener_medico import Obtener_Infor_Medicos

app = FastAPI()

app.title = "Proyecto de Prueba"
app.version = "1.1.1"

# Simulamos una base de datos en memoria
medicos_db = []

@app.get("/medicos", response_model=list[MedicoSchema] , tags=["Medicos"])
def listar_medicos():
    return medicos_db

@app.post("/medicos", response_model=MedicoSchema, tags=["Medicos"])
def crear_medico(medico: MedicoSchema):
    nuevo_medico = Medico(**medico.dict())
    medicos_db.append(nuevo_medico)
    return nuevo_medico

controller_medico = Obtener_Infor_Medicos()
@app.get("/medicos/{id}", response_model=MedicoSchema)

def obtener_medico(id: int):
    print(id)
    return controller_medico.obtener_medico(id)  

controller_medic = Crear_Medicos()
@app.post("/medicos/agrega", tags=["Paciente"])
def llenar_medicos():
  return controller_medic.llenar_medicos()

