import serial

# Configura la conexión serial
ser = serial.Serial('COM1', 9600)  # Reemplaza 'COM1' por el puerto serial que estés utilizando y 9600 por la velocidad de baudios que necesites

# Array serial
num_serials = ['8', '7', '12', '10']
array_serials = []
for num_serial in num_serials:
    array_serials.append(serial.Serial('COM' + num_serial, 115200))
try:
    while True:
        for ser in array_serials:
            # Lee una línea del puerto serial
            line = ser.readline()
            
            # Decodifica la línea recibida (puede que necesites ajustar el encoding según tus necesidades)
            decoded_line = line.decode('utf-8').strip()
            
            # Imprime la línea recibida
            print(decoded_line)

except KeyboardInterrupt:
    # Cierra la conexión serial al presionar Ctrl+C
    ser.close()
