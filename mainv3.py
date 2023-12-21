import time
from machine import Pin
led=Pin(13,Pin.OUT)    #create LED object from pin13,Set Pin13 to output
led1=Pin(25,Pin.OUT)
led2=Pin(14,Pin.OUT)
led3=Pin(15,Pin.OUT)


while True:
  led.value(1)            #Set led turn on
  time.sleep(0.9)
  print("Hello")
  led.value(0)            #Set led turn off
  time.sleep(0.5)
  print("World")
  led1.value(1)
  time.sleep(0.25)
  print("I am a pico")
  led1.value(0)
  time.sleep(0.2)
  print("microcontroller")
  led2.value(1)
  time.sleep(3)
  print(4)
  led2.value(0)
  time.sleep(1)
  led3.value(1)
  time.sleep(1.2)
  led3.value(0)
  time.sleep(0.5)