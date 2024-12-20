from fastapi import FastAPI, HTTPException
from app.Controllers.crear_Usuario import Crear_Medicos
from app.Models.models import Medico
from app.Models.schemas import MedicoSchema
from app.Controllers.obtener_medico import Obtener_Infor_Medicos

app = FastAPI()

app.title = "Proyecto de Prueba"
app.version = "1.1.1"

sert = Obtener_Infor_Medicos()
polk = Crear_Medicos()
# Simulamos una base de datos en memoria
medicos_db = []

#=========================================================

@app.get("/", tags=["Bienvenido"])
def listar_medicos():
    return "Bienvenido perro al mundo fast api"

#=========================================================

@app.get("/medicos", response_model=list[MedicoSchema] , tags=["Medicos"])
def listar_medicos():
    return sert.ObtenerTodosLosMedicos()

#=========================================================

@app.post("/medicos/agregar", tags=["Medicos"])
def Adicionar_medico(nuevo_usuario:MedicoSchema):
    return polk.llenar_medicos(nuevo_usuario)

#=========================================================

controller_medico = Obtener_Infor_Medicos()
@app.get("/medicos/{id}", response_model=MedicoSchema)

def obtener_medico(id: int):
    print(id)
    return controller_medico.obtener_medico(id)  



