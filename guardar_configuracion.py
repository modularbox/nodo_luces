import json
import os

class GuardarConfiguracion:
    def __init__(self, lugar):
        self.lugar = lugar
        self.nombre_archivo = 'datos.json'
        self.hardcode_luces = {
            "saucedilla": {
                "horarios": [
                    {"horario_inicio": "19:30:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"}
                ],
                "modo": "automatico",
                "canales": [1, [2, 170], 4, 11, [12, 170], 14, 21, [22, 170], 24, 31, [32, 170], 34, 41, [42, 170], 44, 51, [52, 170], 54, 61, [62, 170], 64, 71, [72, 170], 74, 81, [82, 170], 84, 91, [92, 170], 94, 101, [102, 170], 104, 111, [112, 170], 114, 121, [122, 170], 124, 131, [132, 170], 134, 141, [142, 170], 144, 151, [152, 170], 154, 161, [162, 170], 164, 171, [172, 170], 174, 181, [182, 170], 184, [201, 170], 203, [204, 170], 206, [207, 170], 209, [210, 170], 212, [213, 170], 215, [216, 170], 218, [219, 170], 221, [222, 170], 224, [231, 170], 233, [234, 170], 236, [237, 170], 239, [240, 170], 242, [243, 170], 245, [246, 170], 248, [249, 170], 251, [252, 170], 254, [261, 170], 263, [264, 170], 266, [267, 170], 269, [270, 170], 272, [273, 170], 275, [276, 170], 278, [279, 170], 281, [282, 170], 284, [291, 170], 293, [294, 170], 296, [297, 170], 299, [300, 170], 302, [303, 170], 305, [306, 170], 308, [309, 170], 311, [312, 170], 314, 321, [322, 170], 324, 331, [332, 170], 334, 341, [342, 170], 344]
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
            "garage":{
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
            if os.path.exists(self.nombre_archivo):
                with open(self.nombre_archivo, 'r') as archivo:
                    datos = json.load(archivo)
                    return datos.get(self.lugar)
            else:
                with open(self.nombre_archivo, 'w') as archivo:
                    json.dump(self.hardcode_luces, archivo)
                    return self.hardcode_luces.get(self.lugar)
        except:
            return None

    def guardar_datos_en_json(self, nuevos_datos):
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                datos = json.load(archivo)
            datos[self.lugar] = nuevos_datos
            with open(self.nombre_archivo, 'w') as archivoWrite:
                json.dump(datos, archivoWrite)
        except Exception as e:
            print("Error al guardar datos en JSON:", e)
