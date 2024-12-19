from fastapi import HTTPException
from app.Models.models import Medico
from app.Models.schemas import MedicoSchema

# Base de datos simulada
medicos_base = [  {"id": 3, "nombre": "Dr. Juan Pérez", "especialidad": "Cardiología"},
            {"id": 2, "nombre": "Dra. Ana López", "especialidad": "Pediatría"},
            {"id": 1, "nombre": "Dr. Luis García", "especialidad": "Neurología"},]  

class Crear_Medicos:
    # Usamos el decorador @staticmethod ya que no necesitamos crear una instancia
    def llenar_medicos():
        medicos_por_defecto = [
            {"id": 3, "nombre": "Dr. Juan Pérez", "especialidad": "Cardiología"},
            {"id": 2, "nombre": "Dra. Ana López", "especialidad": "Pediatría"},
            {"id": 1, "nombre": "Dr. Luis García", "especialidad": "Neurología"},
        ]
        
        for medico_data in medicos_por_defecto:
            # Creación de un nuevo médico usando la clase Medico
            nuevo_medico = Medico(**medico_data)
            medicos_base.append(nuevo_medico)  # Agregarlo a la base de datos simulada
            print(nuevo_medico)  # Imprimir para ver en consola el médico añadido

        return {"mensaje": "Datos de médicos añadidos correctamente"}
