import time
from machine import Pin
led=Pin(13,Pin.OUT)    #create LED object from pin13,Set Pin13 to output
led1=Pin(25,Pin.OUT)
led2=Pin(14,Pin.OUT)
x=(4)
y=(4)

while True:
 
  led.value(1)
  time.sleep(x+y)
  print(x+y)
  led.value(0)
  time.sleep(x)
  led2.value(1)
  time.sleep(y)
  print(x-y)
  led.value(0)
  time.sleep(x-y+1)
  led1.value(1)
  time.sleep(x+1)
  led1.value(0)
  time.sleep(y-1)
  print(x*y)