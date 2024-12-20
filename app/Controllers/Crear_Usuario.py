from fastapi import HTTPException
from app.Controllers.obtener_medico import Obtener_Infor_Medicos
 
class Crear_Medicos:
    
    def llenar_medicos(nuevo_usuario): 
        instancia_clase = Obtener_Infor_Medicos()
        
        instancia_de_usuario =instancia_clase.ObtenerTodosLosMedicos()
        print (instancia_de_usuario)
        if not isinstance(instancia_de_usuario, list):
            raise HTTPException(status_code=500, detail="Los datos de médicos no son una lista válida")
        
        nuevo_usuario = nuevo_usuario.dict()
        
        instancia_de_usuario.append(nuevo_usuario)
        instancia_clase.write_medico(instancia_de_usuario)
        return {"mensaje": "Datos de médicos añadidos correctamente"}

