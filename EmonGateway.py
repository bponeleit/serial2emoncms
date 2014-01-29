import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

try: 
 ser.open()
except Exception, e:
 print "error open serial port: " + str(e)
 exit()

if ser.isOpen():
 try:
  while True:
   response = ser.readline()
   ser.close()
 except Exception, e1:
	    print "error communicating...: " + str(e1)
else:
    print "cannot open serial port "
