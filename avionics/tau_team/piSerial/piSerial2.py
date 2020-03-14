import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyAMA0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
print(ser)
def blink(pin):


  GPIO.output(pin,GPIO.HIGH)  
  time.sleep(1)  
  GPIO.output(pin,GPIO.LOW)  
  time.sleep(1)  
  return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
while True:
  print('yee')
  ser.write(b"hello from pi")
  read_ser=ser.readline()
  print('yee2')
  print(read_ser)
  if(read_ser=="Hello From Arduino!"):
   blink(11)
