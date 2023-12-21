import time
from machine import Pin
led=Pin(13,Pin.OUT)    #create LED object from pin13,Set Pin13 to output
led1=Pin(25,Pin.OUT)
a_vector=(4,2,2,55)
b_vector=(2,3,4,43)
x=(4*6)
y=(9*9)
while True:
 
  led.value(1)
  time.sleep(x+y)
  print(sum(a*b for a,b in zip(a_vector,b_vector)))
  led.value(0)
  time.sleep(x/2)