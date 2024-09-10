
# Importar el controlador OpenDMX o uDMX de PyDMXControl,
# este será el medio por el cual se enviarán los datos.
from PyDMXControl.controllers import OpenDMXController
# from PyDMXControl.controllers import uDMXController

# Importar el perfil de fixture que utilizaremos,
# en este ejemplo, el simple Dimmer.
from PyDMXControl.profiles.Generic import Dimmer

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
fixture = dmx.add_fixture(Dimmer, name="Mi_Primer_Dimmer", start_channel=1, channels=150)

# A continuación, atenuar la intensidad del fixture desde su valor inicial de cero
# hasta el máximo, que está representado como 255 en DMX.
# Esto se realiza en 5000 milisegundos, o 5 segundos.
# fixture.dim(255, 5000)

# Funciones para el control de los canales
def encender_luz(channel):
    # print("Se encendieron las luces")
    fixture.dim(255, 1000, channel - 1)
    print("Encender luz ", channel)

for channel in dmxChannels:
    encender_luz(channel)
# Ahora podemos iniciar el panel de control web incorporado en PyDMXControl.
# Esto mostrará la dirección web en la consola, pero debería ser http://0.0.0.0:8080
# Esto se ejecuta en segundo plano, por lo que podemos continuar haciendo otras cosas.
dmx.web_control()

# También se puede iniciar el modo de depuración en la consola si es necesario,
# esto proporciona opciones de control básicas en la consola del programa.
# Sin embargo, esto es bloqueante, por lo que el script no continuará más allá de aquí
# hasta que se salga del control de depuración. Esto no detendrá la salida DMX.
dmx.debug_control()

# Una vez que se salga del modo de depuración en la consola, el script continuará. Para evitar que
# salga y detenga la salida DMX, podemos usar una función de espera incorporada.
# Esta función de espera esperará hasta que se presione enter en la consola antes de continuar.
# dmx.sleep_till_enter()

# Con todo listo, puedes terminar la salida DMX y el programa llamando
# al método close del controlador.
# Esto cerrará de manera limpia cualquier hilo en uso y detendrá la salida DMX.
# dmx.close()
