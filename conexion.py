import threading
import time
import socketio
import sys
import programa_luces
from enum import Enum
import requests
from programa_hardcode import ProgramaHardcode
from custom_logger import CustomLogger

# Version Programa
VERSION = '3.0.0-2'

# Crear una instancia del logger
logger = CustomLogger()

# Verificar si hay internet
def hay_internet():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Definir una enumeración simple
class Programas(Enum):
    PROGRAMA = 1
    PROGRAMA_POR_TIEMPO = 2
    PROGRAMA_PANEL = 3

# Crea el evento
theared_program = threading.Event()

# Cliente de los sockets
sio = socketio.Client(logger=True, reconnection=False)

# Creamos la funcion que se ejecutara para encender las luces
class TimedEventThread(threading.Thread):
    def __init__(self, interval, event, programa, programa_por_tiempo, programa_panel, request_programa=None, request_programa_por_tiempo=None, request_programa_panel=None):
        super().__init__()
        self.interval = interval
        self.stopped = event
        self.programa_execute = Programas.PROGRAMA  
        self.programa = programa
        self.programa_por_tiempo = programa_por_tiempo
        self.programa_panel = programa_panel
        self.request_programa = request_programa or ProgramaHardcode(lugar).get_luces_lugar()
        self.request_programa_por_tiempo = request_programa_por_tiempo or {}
        self.request_programa_panel = request_programa_panel or {}

    def run(self):
        while not self.stopped.wait(self.interval):
            # Iniciar los sockets
            if not sio.connected:
                try:
                    sio.connect('http://apiluces.modularbox.com:3005')
                    logger.log_info("Conexión exitosa a los sockets.")
                    sio.sleep(2)
                except socketio.exceptions.ConnectionError:
                    logger.log_info("Error al intentar reconectar. Reintentando en 2 segundos...")
                    
            if self.programa_execute == Programas.PROGRAMA:
                self.programa(self.request_programa)
                
            elif self.programa_execute == Programas.PROGRAMA_POR_TIEMPO:
                self.programa_por_tiempo(self.request_programa_por_tiempo)

            elif self.programa_execute == Programas.PROGRAMA_PANEL:
                self.programa_panel(self.request_programa_panel)
            
    def changePrograma(self, nuevo_programa):
        self.programa_execute = nuevo_programa

    def changeRequestPrograma(self, nuevo_request):
        ProgramaHardcode(lugar).guardar_luces(nuevo_request)
        self.request_programa = nuevo_request
    # --------------------------------------------
    def changeRequestProgramaPanel(self, nuevo_request):
        self.request_programa_panel = nuevo_request

    def changeRequestProgramaPorTiempo(self, nuevo_request):
        self.request_programa_por_tiempo = nuevo_request
        
# Función para iniciar el evento
def start_event(event_thread):
    if not event_thread.is_alive():
        event_thread.start()
        logger.log_info(f"Programa iniciado VERSION: {VERSION}")
    else:
        logger.log_info("El evento ya está en ejecución")

# Example: Correr programa python3 luces.py lugar
lugar = 'garaje'
if len(sys.argv) > 1:
    lugar = sys.argv[1]
    logger.log_info(f"El valor del parámetro es: {lugar}")

# Ejecutar el programa
# Enviamos el request y el lugar, para obtener los datos hardcodeados
def ejecutar_programa(request):
    programa_luces.init_luces(request)

# Ejecutar el programa por tiempo solo se envia el request
def ejecutar_programa_por_tiempo(request):
    programa_luces.programa_por_tiempo(request)

# Ejecutar el programa por tiempo solo se envia el request ----------------------
def ejecutar_programa_panel(request):
    programa_luces.funcionalidad_luces(request)
    
# Función para programar la ejecución del programa definitivo
def programa_ejecucion(request):
    global theared
    theared.changeRequestPrograma(request)
    if theared.programa_execute != Programas.PROGRAMA_POR_TIEMPO:
        theared.changePrograma(Programas.PROGRAMA)

# Función para programar la ejecución del programa panel definitivo --------------------------------------------------
def programa_panel_ejecucion(request):
    global theared
    theared.changeRequestProgramaPanel(request)
    if theared.programa_execute != Programas.PROGRAMA_PANEL:
        theared.changePrograma(Programas.PROGRAMA_PANEL)
    
# Función para programar la ejecución del programa después de 10 segundos
def programa_por_tiempo_ejecucion(request):
    global theared
    if theared.request_programa.get('modo') == 'manual':
        theared.changeRequestProgramaPorTiempo(request)
        programa_luces.guardar_configuracion_programa_por_tiempo_canales = []
        programa_luces.off_all_channels()
        theared.changePrograma(Programas.PROGRAMA_POR_TIEMPO)
        time.sleep(request.get('time'))
        programa_luces.off_all_channels()
        theared.changePrograma(Programas.PROGRAMA)

# Funcion de los sockets
@sio.event
def connect():
    logger.log_info('connection established sockets')

@sio.on('programa' + lugar)
def programa(request):
    # string_request = str(request)
    # logger.log_info('Nueva configuracion programa en ejecucion')
    # logger.log_warning(string_request)
    # programa_ejecucion(request)

    string_request = str(request)
    logger.log_info('Nueva configuracion programa panel en ejecucion')
    logger.log_warning(string_request)
    programa_ejecucion(request)

# -------------------------------------------------- ptrrogrma de panel --------------------------------------------------
@sio.on('programa_panel' + lugar) 
def programa_panel(request):
    string_request = str(request)
    logger.log_info('Nueva configuracion programa panel en ejecucion')
    logger.log_warning(string_request)
    programa_panel_ejecucion(request)

@sio.on('programa_por_tiempo' + lugar)
def programa_por_tiempo(request):
    string_request = str(request)
    logger.log_info('Nueva configuracion programa por tiempo')
    logger.log_warning(string_request)
    programa_por_tiempo_ejecucion(request)

@sio.event
def connect_error(data):
    logger.log_warning('The connection failed')

@sio.event
def disconnect():
    logger.log_info('disconnected from server')
    # Intentar reconectar después de 3 segundos
        # time.sleep(3)
        # main_inicio() 

def main_inicio():
    global theared
    while True:
        logger.log_info("Checando conexion")
        if hay_internet():
            break
        time.sleep(3)
    # Crea el hilo para el evento
    theared = TimedEventThread(2, theared_program, ejecutar_programa, ejecutar_programa_por_tiempo, ejecutar_programa_panel)
    # Iniciar Evento
    start_event(theared)

if __name__ == "__main__":
    main_inicio()