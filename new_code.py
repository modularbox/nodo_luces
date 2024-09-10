
# Importar el controlador OpenDMX o uDMX de PyDMXControl,
# este será el medio por el cual se enviarán los datos.
from PyDMXControl.controllers import OpenDMXController
# from PyDMXControl.controllers import uDMXController

# Importar el perfil de fixture que utilizaremos,
# en este ejemplo, el simple Dimmer.
from PyDMXControl.profiles.Generic import Dimmer
from PyDMXControl.profiles.Generic import Custom

# What DMX channels we want to listen to
dmxChannels = [1, 2, 11, 12, 21, 24, 27, 30, 33, 36, 39, 42, 51, 54, 57, 60, 63, 66, 69, 72, 91, 92, 101, 102]
# Crear una instancia del controlador OpenDMX,
# esta instancia mantendrá toda la información de los fixtures y la enviará.
# Esto comenzará a enviar datos inmediatamente.
dmx = OpenDMXController()
# dmx = uDMXController()

# Añadir un nuevo fixture Dimmer a nuestro controlador
# y guardarlo en una variable para que podamos acceder a él.
# Le damos un nombre para que sea más fácil identificarlo en las opciones de control de depuración.
fixture = dmx.add_fixture(Custom, name="Mi_Primer_Dimmer", start_channel=1, channels=150)

# Ahora, enciende los canales especificados en el array
# Se asume que quieres encender todos los canales al valor máximo (255)
dmxChannels = [1, 2, 11, 12, 21, 24, 27, 30, 33, 36, 39, 42, 51, 54, 57, 60, 63, 66, 69, 72, 91, 92, 101, 102]

# Establece el valor de cada canal a 255
fixture.set_channels(*[255 if channel in dmxChannels else None for channel in range(1, 513)])

# O si el número de canales es menor a 512, solo usa los canales necesarios
# Ajuste de ejemplo en base al número de canales necesarios
# fixture.set_channels(*[255 if i in dmxChannels else None for i in range(1, max(dmxChannels) + 1)])
