import serial
ser = serial.Serial('/dev/rfcomm0')
ser.isOpen()
