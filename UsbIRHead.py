"""
Use oemgateway with IEC 62056-21 compatible smart meter
"""
import serial
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
        wait(0.5)
        ser.readline()
        ser.write("\06050\r\n")
        while "\03" not in response:
            response = response + ser.read()
        print response
        ser.close()
    except Exception, e1:
        print "error communicating...: " + str(e1)
else:
    print "cannot open serial port "



#class OemGatewayIskraMT174Listener(OemGatewaySmartMeterListener):
