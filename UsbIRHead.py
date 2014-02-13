"""
Use oemgateway with IEC 62056-21 compatible smart meter
"""
import serial
from oemgateway.oemgatewaylistener import OemGatewaySerialListener

# Open serial port
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

class OemGatewaySmartMeterListener(OemGatewaySerialListener):
    """class OemGatewaySmartMeterListener

    Reads data from smart meter on serial port

    """
    def __init__(self, com_port, option_select):
        """
        Initialize listener
        """
        super(OemGatewaySmartMeterListener, self).__init__(com_port)
        self._request_message = "/?!\r\n"
        self._option_select = option_select
        self._id = None

    def read(self):
        """
        read data set
        """
        ser._rx_buf = ""
        self._ser.write(self._request_message)

        self._id = self._ser.readline().rstrip

        self._ser.write(self._option_select)

        # Read serial RX
        while "\03" not in self._rx_buf:
            self._rx_buf = self._rx_buf + self._ser.read()

        self._ser.read()

#class OemGatewayIskraMT174Listener(OemGatewaySmartMeterListener):
