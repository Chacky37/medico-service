import json, pathlib

class ObtenerInformacionMedicos:
  #Ruta donde se encuentra el archivo database.json
  __address_file__ = "{0}/app/Services/database.json".format(pathlib.Path().absolute())
  
  #Leer el archivo .json
  def ObtenerTodosLosMedicos(self):
   with open(self.__address_file__, "r") as leer_archivo:
     return json.loads(leer_archivo.read())
  
  #Escribe en el archivo .json
  def write_medico(self, new_data):
   with open(self.__address_file__, "w") as escribir_archivo:
    escribir_archivo.write(json.dumps(new_data))


  
