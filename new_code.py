import time
from PyDMXControl.controllers import OpenDMXController
from PyDMXControl.profiles.Generic import Custom

# Qué canales DMX queremos controlar
dmxChannels = [1, 2, 11, 12, 21, 24, 27, 30, 33, 36, 39, 42, 51, 54, 57, 60, 63, 66, 69, 72, 91, 92, 101, 102]

# Crear una instancia del controlador OpenDMX
dmx = OpenDMXController()

# Añadir un nuevo fixture Dimmer a nuestro controlador
fixture = dmx.add_fixture(Custom, name="Mi_Primer_Dimmer", start_channel=1, channels=150)

# Función para encender los canales
def turn_on_channels(fixture, channels):
    print("Encendiendo canales...")
    # Asegurarse de que cada valor en 'values' sea un entero entre 0 y 255
    values = [255 if (i + 1) in channels else 0 for i in range(140)]
    print(values)
    fixture.set_channels(*values)
    print(*values)
    dmx._transmit(values, 1)  # Transmitir los datos
    print("Canales encendidos.")

# Función para apagar los canales
def turn_off_channels(fixture, channels):
    print("Apagando canales...")
    # Asegurarse de que cada valor en 'values' sea un entero entre 0 y 255
    values = [0 if (i + 1) in channels else 0 for i in range(140)]
    fixture.set_channels(*values)
    dmx._transmit(values, 1)  # Transmitir los datos
    print("Canales apagados.")

# Encender los canales
turn_on_channels(fixture, dmxChannels)

# Esperar un tiempo antes de apagar los canales (por ejemplo, 10 segundos)
time.sleep(10)

# Apagar los canales
turn_off_channels(fixture, dmxChannels)
