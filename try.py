import os
import stat
#import os.stat
import serial
import subprocess
import time

def rf_exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True

def readinp():
    global ser 
    ser = serial.Serial('/dev/rfcomm0')
    readl = str(ser.readline())
    if readl != "":
        if readl == str(r"b'power on\n'"):
            with open('pin.txt', 'w') as f: f.write('1')
            readinp()
        elif readl == str(r"b'power off\n'"):
            with open('pin.txt', 'w') as f: f.write('0')
            readinp()
        else:
            print("existance is pain :", readl)
            readinp()

while True:
    if rf_exists('/dev/rfcomm0'):
        readinp()

#    else:
#        print("dev disconnected")

#readinp()

