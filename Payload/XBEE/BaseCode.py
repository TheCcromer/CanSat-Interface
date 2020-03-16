from xbee import XBee
import serial

PORT = 'COM4'
BAUD_RATE = 9600

ser = serial.Serial(PORT, BAUD_RATE)

while True:
 try:
  response = xbee.wait_read_frame() //recibe los paquetes enviados por el XBEE
  print response
except KeyboardInterrupt:
  break

ser.close()
