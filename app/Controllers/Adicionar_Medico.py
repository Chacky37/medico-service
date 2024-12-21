from fastapi import HTTPException
from app.Controllers.Listado_Medico import ObtenerInformacionMedicos
 
class CrearMedico:
    
    def Agregar_medico(self, nuevo_usuario): 
        
        try:
            instancia_clase = ObtenerInformacionMedicos()
            Listado_de_Medico = instancia_clase.ObtenerTodosLosMedicos()
    
            for item in Listado_de_Medico:
             if item["id"] == nuevo_usuario.id:
                return {"Medico existente"}
            
            # Convertir el modelo a diccionario y añadirlo a la lista existente
            nuevo_usuario = nuevo_usuario.dict()
            Listado_de_Medico.append(nuevo_usuario)
            
            # Escribir la lista actualizada en el almacenamiento
            instancia_clase.write_medico(Listado_de_Medico)
            
            return {"mensaje": "Datos de médicos añadidos correctamente "}
        except Exception as e:
            # Manejo de excepciones
            raise HTTPException(status_code=500, detail=str(e))
