from fastapi import FastAPI, HTTPException
from app.Controllers.Adicionar_Medico import CrearMedico
from app.Controllers.Excluir_Medico import BorrarMedico
from app.Controllers.Listado_Medico import ObtenerInformacionMedicos
from app.Controllers.Obtener_Informacion_Id import AccederId
from app.Controllers.Renovar_Medico import RestaurarInformacion
from app.Models.Schemas import MedicoSchema

app = FastAPI()

app.title = "Proyecto Final Prt. 1"
app.version = "1.1.1"

enlace_adicionar_medico = CrearMedico()
enlace_excluir_medico = BorrarMedico()
enlace_listado_medico = ObtenerInformacionMedicos()
enlace_obtener_informacion_id = AccederId()
enlace_renovar_medico = RestaurarInformacion()

@app.get("/", tags=["Bienvenido"])
def Bienvenida():
    return "Bienvenido My Lord"


@app.get("/medicos", response_model=list[MedicoSchema] , tags=["Medicos"])
def Lista_Medico():
    try:
        return enlace_listado_medico.ObtenerTodosLosMedicos()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/medicos/agregar", tags=["Medicos"])
def Registrar_medico(nuevo_usuario:MedicoSchema):
    try:
        return enlace_adicionar_medico.Agregar_medico(nuevo_usuario)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/medicos/{id}", tags=["Medicos"])
def Extraer_datos_por_id(id: int):
    try:
        return enlace_obtener_informacion_id.ConsultarDatosId(id)  # Llamar al método desde la instancia
    except HTTPException as e:
        raise e


@app.put("/medicos/{id}", tags=["Medicos"])
def Actualizar_medico(id: int,  nuevo_usuario:MedicoSchema):
    try:
        return enlace_renovar_medico.Actualizar_Informacion_Medico(id, nuevo_usuario) 
    except HTTPException as e:
        raise e

@app.delete("/medicos/{id}", tags=["Medicos"])
def Eliminar_Medico(id: int):
    try:
        return enlace_excluir_medico.suprimir_medico(id) 
    except HTTPException as e:
        raise e


