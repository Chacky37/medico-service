from fastapi import HTTPException
from app.Controllers.Listado_Medico import ObtenerInformacionMedicos

class AccederId:

 def ConsultarDatosId(self, id):
    try:
        instancia_clase = ObtenerInformacionMedicos()
        Listado_de_Medico = instancia_clase.ObtenerTodosLosMedicos()
        
        # Buscar el médico por ID
        for item in Listado_de_Medico:
            if item["id"] == id:
                return item
        raise HTTPException(status_code=404, detail=f"Médico con ID {id} no encontrado.")
    except HTTPException as e:
        # Relanzar HTTPException si ocurre
        raise e
    except Exception as e:
        # Manejo de errores generales con mensaje detallado
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
