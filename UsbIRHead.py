from serial import Serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=300,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS
)

try: 
 ser.open()
except Exception, e:
 print "error open serial port: " + str(e)
 exit()
 
wait(500)

if ser.isOpen():
 try:
  ser.write("/?!\r\n")
  while True:
   response = ser.readline()
   print response
   ser.close()
 except Exception, e1:
	    print "error communicating...: " + str(e1)
else:
    print "cannot open serial port "

