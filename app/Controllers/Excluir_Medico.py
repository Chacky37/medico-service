from fastapi import HTTPException
from app.Controllers.Listado_Medico import ObtenerInformacionMedicos

class BorrarMedico:

    def suprimir_medico(self, id):
        instancia_clase = ObtenerInformacionMedicos()
        
        Listado_de_Medico = instancia_clase.ObtenerTodosLosMedicos()
        
        # Recorrer la lista para buscar el médico con el ID proporcionado
        for index, item in enumerate(Listado_de_Medico):
            if item["id"] == id:
                
                # Eliminar al médico encontrado de la lista
                Listado_de_Medico.pop(index)
                
                # Guardar la lista actualizada de vuelta en el almacenamiento
                instancia_clase.write_medico(Listado_de_Medico)

                return {"El médico se ha eliminado correctamente"}

        raise HTTPException(status_code=404, detail=f"Médico con ID {id} no encontrado.")
