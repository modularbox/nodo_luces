import json
import os

class GuardarConfiguracion:
    def __init__(self, lugar):
        self.lugar = lugar
        self.nombre_archivo = 'datos_guardados.json'
        self.hardcode_luces = {
            "saucedilla": {
                "horarios": [
                    {"horario_inicio": "21:00:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"}
                ],
                "modo": "automatico",
                "canales": [1,2,3,4,11,12,13,14,21,22,23,24,31,32,33,34,41,42,43,44,51,52,53,54,61,62,63,64,71,72,73,74,81,82,83,84,91,92,93,94,101,102,103,104,111,112,113,114,121,122,123,124,131,132,133,134,141,142,143,144,151,152,153,154,161,162,163,164,171,172,173,174,181,182,183,184,321,322,323,324,331,332,333,334,341,342,343,344,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284]
            },
            "campanario":{
                "horarios": [
                    {"horario_inicio": "19:30:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"}
                ],
                "modo": "automatico",
                "canales": [3, 11, 19, 27, 32, 37, 42, 47, 52, 60, 68, 76, 84, 92, 100]
            }, 
            "cruz_bendita":{
                "horarios": [
                    {"horario_inicio": "19:30:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"}
                ],
                "modo": "automatico",
                "canales": [1, 4, 9, 12, 17, 20, 25, 28, 33, 36, 43, 47, 51, 55]
            },
            "desaguadero":{
                "horarios": [
                    {"horario_inicio": "10:00:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"}
                ],
                "modo": "automatico",
                "canales": [1, 2, 3, 4, 7, 12, 17, 22]
            },
            "ermita":{
                "horarios": [
                    {"horario_inicio": "19:30:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"}
                ],
                "modo": "automatico",
                "canales": [13, 23, 33, 43]
            },
            "oficina_caceres":{
                "horarios": [
                    {"horario_inicio": "19:30:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"}
                ],
                "modo": "automatico",
                "canales": []
            }
        }

    def crear_archivo(self):
        try:
            print("Entro aqui")
            if os.path.exists(self.nombre_archivo):
                with open(self.nombre_archivo, 'r') as archivo:
                    datos = json.load(archivo)
                    return datos
            else:
                with open(self.nombre_archivo, 'w') as archivo:
                    json.dump(self.hardcode_luces.get(self.lugar), archivo)
                    return self.hardcode_luces.get(self.lugar)
        except:
            return None

    def guardar_datos_en_json(self, nuevos_datos):
        try:
            with open(self.nombre_archivo, 'w') as archivoWrite:
                json.dump(nuevos_datos, archivoWrite)
        except Exception as e:
            print("Error al guardar datos en JSON:", e)