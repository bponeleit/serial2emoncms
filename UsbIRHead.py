<<<<<<< HEAD
"""
Use oemgateway with IEC 62056-21 compatible smart meter
"""
import serial
import time
#from oemgateway.oemgatewaylistener import OemGatewaySerialListener

# Open serial port
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=300,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS,
    timeout=10
)

#try:
#    ser.open()
#except Exception, e:
#    print "error open serial port: " + str(e)
#    exit()

if ser.isOpen():
    try:
        ser.write("/?!\r\n")
        time.sleep(0.5)
        ser.readline()
        ser.write("\06050\r\n")
        response = ''
        while "\03" not in response:
            response = response + ser.read()
        print response
        ser.close()
    except Exception, e1:
        print "error communicating...: " + str(e1)
else:
    print "cannot open serial port"
=======
import serial
import time
ser = serial.Serial()
ser.port = '/dev/ttyUSB0'
ser.baudrate = 300
ser.parity = serial.PARITY_EVEN
ser.stopbits = serial.STOPBITS_ONE
ser.bytesize = serial.SEVENBITS
ser.timeout = 1

try:
 ser.open()
except Exception, e:
 print "error open serial port: " + str(e)
 exit()

time.sleep(0.5)

if ser.isOpen():
# try:
  ser.write("/?!\r\n")
  while True:
   response = ser.readline()
   print response
  ser.close()
  
#  except Exception, e1:
#   print "error communicating...: " + str(e)

else:
 print "cannot open serial port"
>>>>>>> e3640ebc853564288086dee1c244ac120e71d52f



#class OemGatewayIskraMT174Listener(OemGatewaySmartMeterListener):
