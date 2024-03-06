from enum import Enum

# Configuracion de las luces, especificando los canales
class Luces:
    def __init__(self, canales=None):
        self.canales = canales or []

# Configuracion de los horarios de inicio y fin
class HoraInicioFin:
    def __init__(self, hora_inicio = None, min_inicio = None, hora_fin = None, min_fin = None,):
        hora_inicio = hora_inicio or 0 
        min_inicio = min_inicio or 0
        hora_fin = hora_fin or 0
        min_fin = min_fin or 0

