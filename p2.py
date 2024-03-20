from PyDMX import *

dmx = PyDMX('/dev/ttyUSB0') # for Linux use '/dev/ttyUSB0' or something

while True:
    dmx.set_data(1,255)
    dmx.set_data(2,255)
    dmx.set_data(3,255)
    dmx.set_data(11,255)
    dmx.set_data(12,255)
    dmx.set_data(13,255)
    dmx.set_data(21,255)
    dmx.set_data(22,255)
    dmx.set_data(23,255)
    dmx.set_data(51,255)
    dmx.set_data(52,255)
    dmx.set_data(53,255)
    dmx.send()

    time.sleep(10)