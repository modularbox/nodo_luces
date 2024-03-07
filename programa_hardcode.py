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
                "canales": [1, [2, 170], 4, 11, [12, 170], 14, 21, [22, 170], 24, 31, [32, 170], 34, 41, [42, 170], 44, 51, [52, 170], 54, 61, [62, 170], 64, 71, [72, 170], 74, 81, [82, 170], 84, 91, [92, 170], 94, 101, [102, 170], 104, 111, [112, 170], 114, 121, [122, 170], 124, 131, [132, 170], 134, 141, [142, 170], 144, 151, [152, 170], 154, 161, [162, 170], 164, 171, [172, 170], 174, 181, [182, 170], 184, [201, 170], 203, [204, 170], 206, [207, 170], 209, [210, 170], 212, [213, 170], 215, [216, 170], 218, [219, 170], 221, [222, 170], 224, [231, 170], 233, [234, 170], 236, [237, 170], 239, [240, 170], 242, [243, 170], 245, [246, 170], 248, [249, 170], 251, [252, 170], 254, [261, 170], 263, [264, 170], 266, [267, 170], 269, [270, 170], 272, [273, 170], 275, [276, 170], 278, [279, 170], 281, [282, 170], 284, [291, 170], 293, [294, 170], 296, [297, 170], 299, [300, 170], 302, [303, 170], 305, [306, 170], 308, [309, 170], 311, [312, 170], 314, 321, [322, 170], 324, 331, [332, 170], 334, 341, [342, 170], 344]}
        if(self.lugar == 'campanario'):
            print('Configuracion Campanario')
            logger.log_info('Configuracion Campanario')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": 
                [[1, 170], 3, [9, 170], 11, [17, 170], 19, [25, 170], 27, [30, 170], 32, [35, 170], 37, [40, 170], 42, [45, 170], 47, [50, 170], 52, [58, 170], 60, [66, 170], 68, [74, 170], 76, [82, 170], 84, [90, 170], 92, [98, 170], 100]}
        if(self.lugar == 'cruz_bendita'):
            print('Configuracion Cruz Bendita')
            logger.log_info('Configuracion Cruz Bendita')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": 
                [[1, 170], 3, [2, 170], 4, [9, 170], 11, [10, 170], 12, [17, 170], 19, [18, 170], 20, [25, 170], 27, [26, 170], 28, [33, 170], 35, [34, 170], 36, [41, 170], 43, [45, 170], 47, [49, 170], 51, [53, 170], 55]
                }
        if(self.lugar == 'desaguadero'):
            print('Configuracion Desaguadero')
            logger.log_info('Configuracion Desaguadero')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": 
                [1, 2, 3, 4, [5, 170], 7, [10, 170], 12, [15, 170], 17, [20, 170], 22]
                }
        if(self.lugar == 'ermita'):
            print('Configuracion Ermita')
            logger.log_info('Configuracion Ermita')
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": 
                [[11, 170], 13, [21, 170], 23, [31, 170], 33, [41, 170], 43]
                }
        return {}
        
