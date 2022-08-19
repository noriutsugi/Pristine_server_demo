import sys
import subprocess
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)
while True:
    bash_bt_output = subprocess.getoutput('bash bt_stat.sh')
    list_bt_output = bash_bt_output.split('\n')
    bash_pin_output = subprocess.getoutput('cat pin.txt')
    with canvas(device) as draw:
        if list_bt_output[0]== '\tPowered: yes':
            draw.point((0,0), fill="red")
        if list_bt_output[1]== '\tDiscoverable: yes':
            draw.point((0,1), fill="red")
        if list_bt_output[2]== '\tPairable: yes':
            draw.point((0,2), fill="red")
        if list_bt_output[3]== '\tDiscovering: yes':
            draw.point((0,3), fill="red")
        if bash_pin_output == '1':
            draw.point((7,0), fill="red")
            draw.point((7,1), fill="red")
            draw.point((7,2), fill="red")
    time.sleep(0.5)


