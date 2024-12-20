from fastapi import HTTPException
#from app.Controllers.Crear_Usuario import Crear_Medicos
import json, pathlib

class Obtener_Infor_Medicos:
  __address_file__ = "{0}/app/Services/database.json".format(pathlib.Path().absolute())
  
  def ObtenerTodosLosMedicos(self):
   with open(self.__address_file__, "r") as leer:
     return json.loads(leer.read())
  
  def write_medico(self, new_data):
   with open(self.__address_file__, "w") as escribir:
    escribir.write(json.dumps(new_data))


  
md = Obtener_Infor_Medicos()

md.ObtenerTodosLosMedicos()
  
