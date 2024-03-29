from custom_logger import CustomLogger
from guardar_configuracion import GuardarConfiguracion
class ProgramaHardcode():
    def __init__(self, lugar):
        super().__init__()
        self.lugar = lugar

    def guardar_luces(self, request):
        GuardarConfiguracion().guardar_datos_en_json(request)
    def get_luces_lugar(self):
        # Crear una instancia del logger
        logger = CustomLogger()
        # Crear una instancia del logger
        guardar_configuracion = GuardarConfiguracion(lugar=self.lugar)
        logger.log_info('Configuracion {}'.format(self.lugar))
        return guardar_configuracion.crear_archivo()
        horario_predeterminado = [
                    {"horario_inicio": "19:30:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"},
                ]
        if(self.lugar == 'saucedilla'):
            print('Configuracion Saucedilla')
            logger.log_info('Configuracion Saucedilla')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": [1, [2, 170], 4, 11, [12, 170], 14, 21, [22, 170], 24, 31, [32, 170], 34, 41, [42, 170], 44, 51, [52, 170], 54, 61, [62, 170], 64, 71, [72, 170], 74, 81, [82, 170], 84, 91, [92, 170], 94, 101, [102, 170], 104, 111, [112, 170], 114, 121, [122, 170], 124, 131, [132, 170], 134, 141, [142, 170], 144, 151, [152, 170], 154, 161, [162, 170], 164, 171, [172, 170], 174, 181, [182, 170], 184, [201, 170], 203, [204, 170], 206, [207, 170], 209, [210, 170], 212, [213, 170], 215, [216, 170], 218, [219, 170], 221, [222, 170], 224, [231, 170], 233, [234, 170], 236, [237, 170], 239, [240, 170], 242, [243, 170], 245, [246, 170], 248, [249, 170], 251, [252, 170], 254, [261, 170], 263, [264, 170], 266, [267, 170], 269, [270, 170], 272, [273, 170], 275, [276, 170], 278, [279, 170], 281, [282, 170], 284, [291, 170], 293, [294, 170], 296, [297, 170], 299, [300, 170], 302, [303, 170], 305, [306, 170], 308, [309, 170], 311, [312, 170], 314, 321, [322, 170], 324, 331, [332, 170], 334, 341, [342, 170], 344]
            }
        if(self.lugar == 'campanario'):
            print('Configuracion Campanario')
            logger.log_info('Configuracion Campanario')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": [3, 11, 19, 27, 32, 37, 42, 47, 52, 60, 68, 76, 84, 92, 100]
            }
        if(self.lugar == 'cruz_bendita'):
            print('Configuracion Cruz Bendita')
            logger.log_info('Configuracion Cruz Bendita')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": [1, 4, 9, 12, 17, 20, 25, 28, 33, 36, 43, 47, 51, 55]
            }
        if(self.lugar == 'desaguadero'):
            print('Configuracion Desaguadero')
            logger.log_info('Configuracion Desaguadero')
            return {
                "horarios": [
                    {"horario_inicio": "10:00:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"},
                ],
                "modo": "automatico",
                "canales": [1, 2, 3, 4, 7, 12, 17, 22]
            }
        if(self.lugar == 'ermita'):
            print('Configuracion Ermita')
            logger.log_info('Configuracion Ermita')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": [13, 23, 33, 43]
            }
        return {}
    
"""
from custom_logger import CustomLogger
class ProgramaHardcode():
    def __init__(self, lugar):
        super().__init__()
        self.lugar = lugar

    def get_luces_lugar(self):
        # Crear una instancia del logger
        logger = CustomLogger()
        horario_predeterminado = [
                    {"horario_inicio": "19:30:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"},
                ]
        if(self.lugar == 'saucedilla'):
            print('Configuracion Saucedilla')
            logger.log_info('Configuracion Saucedilla')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": [1, [2, 170], 4, 11, [12, 170], 14, 21, [22, 170], 24, 31, [32, 170], 34, 41, [42, 170], 44, 51, [52, 170], 54, 61, [62, 170], 64, 71, [72, 170], 74, 81, [82, 170], 84, 91, [92, 170], 94, 101, [102, 170], 104, 111, [112, 170], 114, 121, [122, 170], 124, 131, [132, 170], 134, 141, [142, 170], 144, 151, [152, 170], 154, 161, [162, 170], 164, 171, [172, 170], 174, 181, [182, 170], 184, [201, 170], 203, [204, 170], 206, [207, 170], 209, [210, 170], 212, [213, 170], 215, [216, 170], 218, [219, 170], 221, [222, 170], 224, [231, 170], 233, [234, 170], 236, [237, 170], 239, [240, 170], 242, [243, 170], 245, [246, 170], 248, [249, 170], 251, [252, 170], 254, [261, 170], 263, [264, 170], 266, [267, 170], 269, [270, 170], 272, [273, 170], 275, [276, 170], 278, [279, 170], 281, [282, 170], 284, [291, 170], 293, [294, 170], 296, [297, 170], 299, [300, 170], 302, [303, 170], 305, [306, 170], 308, [309, 170], 311, [312, 170], 314, 321, [322, 170], 324, 331, [332, 170], 334, 341, [342, 170], 344]
            }
        if(self.lugar == 'campanario'):
            print('Configuracion Campanario')
            logger.log_info('Configuracion Campanario')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": [3, 11, 19, 27, 32, 37, 42, 47, 52, 60, 68, 76, 84, 92, 100]
            }
        if(self.lugar == 'cruz_bendita'):
            print('Configuracion Cruz Bendita')
            logger.log_info('Configuracion Cruz Bendita')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": [1, 4, 9, 12, 17, 20, 25, 28, 33, 36, 43, 47, 51, 55]
            }
        if(self.lugar == 'desaguadero'):
            print('Configuracion Desaguadero')
            logger.log_info('Configuracion Desaguadero')
            return {
                "horarios": [
                    {"horario_inicio": "10:00:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"},
                ],
                "modo": "automatico",
                "canales": [1, 2, 3, 4, 7, 12, 17, 22]
            }
        if(self.lugar == 'ermita'):
            print('Configuracion Ermita')
            logger.log_info('Configuracion Ermita')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": [13, 23, 33, 43]
            }
        return {}
        
"""