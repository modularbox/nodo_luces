class ProgramaHardcode():
    def __init__(self, lugar):
        super().__init__()
        self.lugar = lugar

    def get_luces_lugar(self):
        horario_predeterminado = [
                    {"horario_inicio": "19:30:00", "horario_fin": "23:59:00"},
                    {"horario_inicio": "00:00:00", "horario_fin": "05:00:00"},
                ]
        if(self.lugar == 'saucedilla'):
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": [1, 3, 11, 13, 21, 23, 31, 33, 41, 43, 51, 53, 61, 63, 71, 73, 81, 83, 91, 93, 101, 103, 111, 113, 121, 123, 131, 133, 141, 143, 151, 153, 161, 163, 171, 173, 181, 183]}
        if(self.lugar == 'campanario'):
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": 
                [3, 11, 19, 27, 32, 37, 42, 47, 52, 60, 68, 76, 84, 92, 100]}
        if(self.lugar == 'cruz_bendita'):
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": 
                [1, 3, 9, 11, 17, 19, 25, 27, 33, 35, 42, 46, 50, 54]
                }
        if(self.lugar == 'desaguadero'):
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": 
                [1, 2, 3, 4, 6, 11, 16, 21]
                }
        if(self.lugar == 'ermita'):
            return {
                "horarios": horario_predeterminado,
                "modo": "automatico",
                "canales": 
                [12, 22, 32, ]
                }
        return {}
        
