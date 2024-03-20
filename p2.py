from PyDMX import *

dmx = PyDMX('COM3') # for Linux use '/dev/ttyUSB0' or something

while True:
    dmx.set_data(1,255)
    dmx.set_data(2,255)
    dmx.set_data(3,255)
    dmx.set_data(4,255)
    dmx.send()

    time.sleep(10)