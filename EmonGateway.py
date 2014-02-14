import serial
import ConfigParser
import os
import urllib
import oemgateway

# Read configuration file
config = ConfigParser.ConfigParser()
config.readfp(open('EmonGateway.config'))

# Open serial port
try:
    ser = serial.Serial(
        port='/dev/tty.usbserial-A602SIUH',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )
except Exception, e2:
    print "errOR!" + str(e)
    exit()

#try:
#    ser.open()
#except Exception, e:
#    print "error open serial port: " + str(e)
#    exit()

if ser.isOpen():
    try:
        while True:
            for i in range(0, 3):
                 response = ser.readline()
                 print response.rstrip()
            print "EOL"
        ser.close()
    except Exception, e1:
        print "error communicating...: " + str(e1)
else:
    print "cannot open serial port "
    
