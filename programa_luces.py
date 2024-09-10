from datetime import datetime
import time
from PyDMXControl.controllers import OpenDMXController
from PyDMXControl.profiles.Generic import Custom
from fixture_model import FixtureModel
from custom_logger import CustomLogger

# Crear una instancia del logger
logger = CustomLogger()
# Cargar luces desde JSON
# ------------------ Todo el codigo de las luces ------------------
try:
    dmx = OpenDMXController()
    # Big square fixture model
    # Añadir un nuevo fixture Dimmer a nuestro controlador
    fixture = dmx.add_fixture(Custom, name="Mi_Primer_Dimmer", start_channel=1, channels=150)
except Exception as e:
    logger.log_info('error', e)

# Guardar configuraciones anteriores
guardar_configuracion_programa_por_tiempo_canales = []
guardar_configuracion_programa_canales = []
luces_encendidas = False

def assign_values_to_channels(color_array):
    """
    Asigna valores a los canales DMX basados en el array de colores proporcionado.
    :param color_array: Array que define los colores y los canales.
    :return: Lista de valores para los canales DMX.
    """
    # Inicializar el array de valores de DMX con 0
    values = [0] * 104

    for item in color_array:
        if isinstance(item, list):
            channel = item[0] - 1  # Ajustar índice basado en 1
            color_value = item[1]
            if 0 <= channel < len(values):
                values[channel] = color_value
        else:
            channel = item - 1  # Ajustar índice basado en 1
            if 0 <= channel < len(values):
                values[channel] = 255

    return values

# Función para encender los canales
def turn_on_channels(channels):
    logger.log_info("Encendiendo canales...")
    values = assign_values_to_channels(channels)
    fixture.set_channels(*values)
    dmx._transmit(values, 1)  # Transmitir los datos
    logger.log_info("Canales encendidos.")

# Función para apagar los canales
def turn_off_channels(channels):
    logger.log_info("Apagando canales...")
    # Asegurarse de que cada valor en 'values' sea un entero entre 0 y 255
    values = [0 if (i + 1) in channels else 0 for i in range(140)]
    fixture.set_channels(*values)
    dmx._transmit(values, 1)  # Transmitir los datos
    logger.log_info("Canales apagados.")

def ciclo_luces():
    global guardar_configuracion_programa_canales
    canales = guardar_configuracion_programa_canales
    turn_on_channels(canales)
# ------------------ Aqui termina el codigo ------------------
# ------------------ Codigo para la programacion de las luces en horas ------------------
        
# Programa para ejecutar el programa por tiempo
def programa_por_tiempo(request):
    global guardar_configuracion_programa_por_tiempo_canales
    canales = request.get('canales')
    ejecutar_cliclo = False
    # Verificamos si la peticion es igual para que no se esten seteando los valores
    if canales != guardar_configuracion_programa_por_tiempo_canales:
        guardar_configuracion_programa_por_tiempo_canales = canales
        ejecutar_cliclo = True
    if ejecutar_cliclo:    
        ciclo_luces(canales)

# Función que comprueba si la hora actual está dentro del rango especificado
def verificar_hora(hora_inicio, hora_fin):
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now()

    # Convertir la hora específica a un objeto datetime
    fecha_hora_inicio = datetime.strptime(hora_inicio, "%H:%M:%S")
    fecha_hora_fin = datetime.strptime(hora_fin, "%H:%M:%S")

    # Asignar una hora específica (por ejemplo, 15:30:00)
    fecha_inicio = fecha_hora_inicio.replace(year=fecha_actual.year, month=fecha_actual.month, day=fecha_actual.day)
    fecha_fin = fecha_hora_fin.replace(year=fecha_actual.year, month=fecha_actual.month, day=fecha_actual.day)
    
    logger.log_info(fecha_inicio <= fecha_actual <= fecha_fin)
    logger.log_info(f"fecha_inicio: {fecha_inicio}, fecha_actual: {fecha_actual}, fecha_fin: {fecha_fin}")
    logger.log_info(f"¿fecha_actual está entre fecha_inicio y fecha_fin?: {fecha_inicio <= fecha_actual <= fecha_fin}")
    # Esto es para que no se apage un minuto y se vuelva a encender
    if fecha_actual.hour == 23 and fecha_actual.minute == 59:
        return True
    if fecha_inicio <= fecha_actual <= fecha_fin: 
        return True
    return False
    
def verificar_horarios(horarios):
    if isinstance(horarios, list):
        for horario in horarios:
            if verificar_hora(horario.get('horario_inicio'), horario.get('horario_fin')):
                logger.log_info("Esta en horario")
                return True
        return False
# ------------------ Termina la programacion de las luces en horas ------------------

def get_light_state_from_api(data):
    global guardar_configuracion_programa_canales
    global luces_encendidas
    canales = data.get('canales')
    # Verificar el horario para encender las luces o apagarlas
    if verificar_horarios(data.get('horarios')):
        luces_encendidas = True 
    else:
        if luces_encendidas:
            guardar_configuracion_programa_canales = []
            luces_encendidas = False
            turn_off_channels(canales)
    if luces_encendidas:
        # Guardamos la configuracion anterior, para que los datos no se esten seteando una y otra vez
        if guardar_configuracion_programa_canales != canales:
            turn_off_channels(canales)
            guardar_configuracion_programa_canales = canales
            # Guardar las luces
            return True
        
    return False
    
# Iniciar el programa
def init_luces(request):
    encender = get_light_state_from_api(request)
    if encender: 
        logger.log_info("---------------------- Encender luces -------------------")
        ciclo_luces()