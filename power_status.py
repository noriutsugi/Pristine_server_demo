import sys
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

if len(sys.argv) != 4:
    exit()

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)
with canvas(device) as draw:
    if sys.argv[1]== '1':
        draw.point((5,0), fill="red")
    if sys.argv[2]== '1':
        draw.point((6,0), fill="red")
    if sys.argv[3]== '1':
        draw.point((7,0), fill="red")
time.sleep(2)

