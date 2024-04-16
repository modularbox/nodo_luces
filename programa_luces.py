from datetime import datetime
import time
from typing import List
from PyDMXControl.controllers import OpenDMXController
from PyDMXControl.profiles.Generic import Custom
from fixture_model import FixtureModel
from custom_logger import CustomLogger
from panel_programa import PanelPrograma, Horario
from panel_programa import get_datos_local

# Crear una instancia del logger
logger = CustomLogger()
# Cargar luces desde JSON
# ------------------ Todo el codigo de las luces ------------------
try:
    dmx = OpenDMXController()
    # Big square fixture model
    bsq_fixture_model = FixtureModel("DRGBWSEP")
    custom_fixture = dmx.add_fixture(Custom,name="CustomFixture", start_channel=1, channels=500)
    bsq_fixture_model.setup_fixture(custom_fixture)
except Exception as e:
    print('error', e)

# Guardar configuraciones anteriores
guardar_configuracion_programa_panel = []
guardar_configuracion_programa_por_tiempo_canales = []
guardar_configuracion_programa_canales = []
luces_encendidas = False

# Funciones para el control de los canales
def encender_luz(channel):
    # print("Se encendieron las luces")
    custom_fixture.dim(255, 0, channel - 1)
def encender_con_value_luz(value, channel):
    # print("Se encendieron las luces")
    custom_fixture.dim(value, 0, channel - 1)
def off_all_channels():
    logger.log_info("Apagar todos los canales")
    for i in range(500):
        custom_fixture.dim(0, 0, i)
def ciclo_luces():
    global guardar_configuracion_programa_canales
    luces = guardar_configuracion_programa_canales
    for channel in luces:
        if isinstance(channel, list):
            encender_con_value_luz(channel[1], channel[0])
        else:
            encender_luz(channel)

# Ciclo de luces por tiempo
def ciclo_luces_programa_por_tiempo():
    global guardar_configuracion_programa_por_tiempo_canales
    luces = guardar_configuracion_programa_por_tiempo_canales
    for programas in luces:
        for channel in programas:
            if isinstance(channel, list):
                encender_con_value_luz(channel[1], channel[0])
                time.sleep(3)
            else:
                encender_luz(channel)
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

def programa_panel(request):
    global guardar_configuracion_programa_por_tiempo_canales

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
            off_all_channels()
    if luces_encendidas:
        # Guardamos la configuracion anterior, para que los datos no se esten seteando una y otra vez
        if guardar_configuracion_programa_canales != canales:
            off_all_channels()
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

# --------------------------------0---------Inicia la programcion del panel de modularbox para las luces -------------------------------

def off_all_channels_panel(canales: list):
    logger.log_info("Apagar todos los canales")
    for i in canales:
        custom_fixture.dim(0, 0, i)

def ciclo_luces_panel(canales: List[int]):
    for canal in canales:
        if isinstance(canal, list):
            encender_con_value_luz(canal[1], canal[0])
        else:
            encender_luz(canal)

def funcionalidad_luces(request):
    print("Funcionalidad luces")
    global guardar_configuracion_programa_panel
    panel_programa = get_datos_local(request)
    list_programa_luces = panel_programa.verificar_horario()
    esta_en_horario = len(list_programa_luces) != 0
    if(esta_en_horario):
        print("Esta en el horario")
        for programa_luces in list_programa_luces:
            if(guardar_configuracion_programa_panel != programa_luces.canales):
                print("programa_luces")
                print(programa_luces.canales)
                off_all_channels_panel(guardar_configuracion_programa_panel)
                guardar_configuracion_programa_panel = programa_luces.canales
                ciclo_luces_panel(programa_luces.canales)
            time.sleep(programa_luces.tiempo)
    else:
        print("No esta en el horario")
        if len(guardar_configuracion_programa_panel) != 0:
            off_all_channels_panel(guardar_configuracion_programa_panel)
            guardar_configuracion_programa_panel = []

# Iniciar el programa
# def init_luces_panel(request):
#     funcionalidad_luces()