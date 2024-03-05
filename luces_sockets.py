import threading
import time
import socketio
import sys
import programa_luces
from enum import Enum
import requests
# Verificar si hay internet
def hay_internet():
    try:
        response = requests.get("http://8.8.8.8", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Definir una enumeración simple
class Programas(Enum):
    PROGRAMA = 1
    PROGRAMA_POR_TIEMPO = 2

# Crea el evento
theared_program = threading.Event()

# Cliente de los sockets
sio = socketio.Client()

class TimedEventThread(threading.Thread):
    def __init__(self, interval, event, programa, programa_por_tiempo, request_programa=None, request_programa_por_tiempo=None):
        super().__init__()
        self.interval = interval
        self.stopped = event
        self.programa_execute = Programas.PROGRAMA
        self.programa = programa
        self.programa_por_tiempo = programa_por_tiempo
        self.request_programa = request_programa or {}
        self.request_programa_por_tiempo = request_programa_por_tiempo or {}

    def run(self):
        while not self.stopped.wait(self.interval):
            if self.programa_execute == Programas.PROGRAMA:
                self.programa(self.request_programa)
            if self.programa_execute == Programas.PROGRAMA_POR_TIEMPO:
                self.programa_por_tiempo(self.request_programa_por_tiempo)
    
    def changePrograma(self, nuevo_programa):
        self.programa_execute = nuevo_programa

    def changeRequestPrograma(self, nuevo_request):
        self.request_programa = nuevo_request

    def changeRequestProgramaPorTiempo(self, nuevo_request):
        self.request_programa_por_tiempo = nuevo_request
        
# Función para iniciar el evento
def start_event(event_thread):
    if not event_thread.is_alive():
        event_thread.start()
        print("Evento iniciado")
    else:
        print("El evento ya está en ejecución")

# Example: Correr programa python3 luces.py lugar
lugar = 'garaje'
if len(sys.argv) > 1:
    lugar = sys.argv[1]
    print("El valor del parámetro es:", lugar)

# Ejecutar el programa
def ejecutar_programa(request):
    global lugar
    print("Programa ejecutandose")
    programa_luces.init_luces(request, lugar)

# Ejecutar el programa
def ejecutar_programa_por_tiempo(request):
    print("Ejecutar programa por tiempo")
    programa_luces.programa_por_tiempo(request)
    
# Función para programar la ejecución del programa después de 10 segundos
def programa_ejecucion(request):
    global theared
    theared.changeRequestPrograma(request)
    if theared.programa_execute != Programas.PROGRAMA_POR_TIEMPO:
        programa_luces.off_all_channels()
        theared.changePrograma(Programas.PROGRAMA)
    
# Función para programar la ejecución del programa después de 10 segundos
def programa_por_tiempo_ejecucion(request):
    global theared
    theared.changeRequestProgramaPorTiempo(request)
    programa_luces.guardar_configuracion_luces = None
    programa_luces.off_all_channels()
    theared.changePrograma(Programas.PROGRAMA_POR_TIEMPO)
    time.sleep(request.get('time'))
    programa_luces.off_all_channels()
    theared.changePrograma(Programas.PROGRAMA)

# Funcion de los sockets
@sio.event
def connect():
    print('connection established')

@sio.on('programa' + lugar)
def programa(data):
    programa_ejecucion(data)

@sio.on('programa_por_tiempo' + lugar)
def programa_por_tiempo(data):
    programa_por_tiempo_ejecucion(data)

@sio.event
def disconnect():
    print('disconnected from server')

if __name__ == "__main__":
    verificar_conexion_internet = True
    while verificar_conexion_internet:
        if hay_internet():
            verificar_conexion_internet = False
        time.sleep(3)
    # Iniciar los sockets
    sio.connect('http://api.conectateriolobos.es:3005')
    # Crea el hilo para el evento
    theared = TimedEventThread(2, theared_program, ejecutar_programa, ejecutar_programa_por_tiempo)
    # Iniciar Evento
    start_event(theared)
    sio.wait()