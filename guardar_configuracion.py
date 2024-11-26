import json
import os
from custom_logger import CustomLogger
# Crear una instancia del logger
logger = CustomLogger()
inicioProgram = False
# Aqui viene la configuracion de luces de saucedilla
# De la iglesia y del ayuntamiento Esta es en orange
class GuardarConfiguracion:
    def __init__(self, lugar):
        logger.log_info("La configuracion esta en color orange")
        programIglesia = [1,2,[3,170],11,12,[13,170],
                          21,22,[23,170],31,32,[33,170],
                          41,42,[43,170],51,52,[53,170],61,62,
                          [63,170],71,72,[73,170],81,82,[83,170]
                          ,91,92,[93,170],101,102,[103,170],111,112,
                          [113,170],121,122,[123,170],131,132,[133,170],
                          141,142,[143,170],151,152,[153,170],161,162,
                          [163,170]]
        programAyuntamiento = [171,172,[173,170],181,182,[183,170],321,322,
                               [323,170],331,332,[333,170],341,342,[343,170],
                               201,[202,170],204,[205,170],207,[208,170],210,
                               [211,170],213,[214,170],216,[217,170],219,[220,170],
                               222,[223,170],231,[232,170],234,[235,170],237,
                               [238,170],240,[241,170],243,[244,170],246,[247,170],
                               249,[250,170],252,[253,170],261,[262,170],264,[265,170],
                               267,[268,170],270,[271,170],273,[274,170],276,[277,170],
                               279,[280,170],282,[283,170]]
        self.lugar = lugar
        self.nombre_archivo = 'datos_guardados.json'
        self.hardcode_luces = {
            "saucedilla": {
                "horarios": [
                    {"horario_inicio": "18:00:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"}
                ],
                "modo": "automatico",
                "canales": programAyuntamiento + programIglesia
            },
            
        }

    def crear_archivo(self):
        try:
            print("Entro aqui")
            if inicioProgram:
                if os.path.exists(self.nombre_archivo):
                    with open(self.nombre_archivo, 'r') as archivo:
                        datos = json.load(archivo)
                        return datos
                else:
                    with open(self.nombre_archivo, 'w') as archivo:
                        json.dump(self.hardcode_luces.get(self.lugar), archivo)
                        return self.hardcode_luces.get(self.lugar)
            else:
                return self.hardcode_luces.get(self.lugar)
        except:
            return None

    def guardar_datos_en_json(self, nuevos_datos):
        try:
            with open(self.nombre_archivo, 'w') as archivoWrite:
                json.dump(nuevos_datos, archivoWrite)
        except Exception as e:
            print("Error al guardar datos en JSON:", e)