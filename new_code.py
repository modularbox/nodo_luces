import time
from PyDMXControl.controllers import OpenDMXController
from PyDMXControl.profiles.Generic import Custom

# Qué canales DMX queremos controlar
dmxChannels = [1, [2, 170], 4, 11, [12, 170], 14, [21, 170], 23, [24, 170], 26, [27, 170], 29, [30, 170], 
               32, [33, 170], 35, [36, 170], 38, [39, 170], 41, [42, 170], 44, [51, 170], 53, [54, 170], 
               56, [57, 170], 59, [60, 170], 62, [63, 170], 65, [66, 170], 68, [69, 170], 71, [72, 170], 
               74, 91, [92, 170], 94, 101, [102, 170], 104]

# Crear una instancia del controlador OpenDMX
dmx = OpenDMXController()

# Añadir un nuevo fixture Dimmer a nuestro controlador
fixture = dmx.add_fixture(Custom, name="Mi_Primer_Dimmer", start_channel=1, channels=150)


def assign_values_to_channels(color_array):
    """
    Asigna valores a los canales DMX basados en el array de colores proporcionado.

    :param channels: Lista de valores de DMX (0-255) para los 512 canales.
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
def turn_on_channels(fixture, channels):
    print("Encendiendo canales...")
    # Asegurarse de que cada valor en 'values' sea un entero entre 0 y 255
    # values = [255 if (i + 1) in channels else 0 for i in range(140)]
    values = assign_values_to_channels(dmxChannels)
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
