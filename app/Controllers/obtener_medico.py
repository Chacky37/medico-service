from fastapi import HTTPException
from app.Controllers.Crear_Usuario import Crear_Medicos
from app.Models.models import Medico
from app.Models.schemas import MedicoSchema

class Obtener_Infor_Medicos:
  
  def obtener_medico(id: int):
    controllers_crear= Crear_Medicos()
    for medico in controllers_crear.medicos_base:
        if medico.id == id:
            print(medico)
            return medico
    raise HTTPException(status_code=404, detail="Médico no encontrado")