import time
from PyDMXControl.controllers import OpenDMXController
from PyDMXControl.profiles.Generic import Custom

from PyDMXControl.profiles.defaults import Fixture

# What DMX channels we want to listen to
dmxChannels = [1, 2, 11, 12, 21, 24, 27, 30, 33, 36, 39, 42, 51, 54, 57, 60, 63, 66, 69, 72, 91, 92, 101, 102]

# Crear una instancia del controlador OpenDMX
dmx = OpenDMXController()

# Añadir un nuevo fixture Dimmer a nuestro controlador
fixture = Fixture( name="Mi_Primer_Dimmer", start_channel=1)

# Función para encender los canales
def turn_on_channels(fixture, channels):
    fixture.set_channels(*[255 if channel in channels else None for channel in range(1, 513)])

# Función para apagar los canales
def turn_off_channels(fixture, channels):
    fixture.set_channels(*[0 if channel in channels else None for channel in range(1, 513)])

# Encender los canales
turn_on_channels(fixture, dmxChannels)

# Esperar un tiempo antes de apagar los canales (por ejemplo, 10 segundos)
time.sleep(10)

# Apagar los canales
turn_off_channels(fixture, dmxChannels)
