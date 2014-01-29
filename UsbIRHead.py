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

