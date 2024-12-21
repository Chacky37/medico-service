from fastapi import HTTPException
from app.Controllers.Listado_Medico import ObtenerInformacionMedicos

class RestaurarInformacion:

    def Actualizar_Informacion_Medico(self, id, medico):
        
        instancia_clase = ObtenerInformacionMedicos()
        
        Listado_de_Medico = instancia_clase.ObtenerTodosLosMedicos()
        
        # Recorrer la lista para encontrar el médico con el ID proporcionado
        for index, item in enumerate(Listado_de_Medico):
            if item["id"] == id:
                # Reemplazar los datos del médico encontrado con los nuevos datos
                Listado_de_Medico[index] = medico.dict()
                
                # Si el nombre no está presente, mantener el nombre original
                if medico.nombre == "":
                    Listado_de_Medico[index]["nombre"] = item["nombre"]  
                
                if medico.especialidad == "":
                    Listado_de_Medico[index]["especialidad"] = item["especialidad"]
                
                # Escribir la lista actualizada de médicos de vuelta en el almacenamiento
                instancia_clase.write_medico(Listado_de_Medico)
                
                return {"El médico se ha actualizado correctamente"}
        
        raise HTTPException(status_code=404, detail=f"Médico con ID {id} no encontrado.")
