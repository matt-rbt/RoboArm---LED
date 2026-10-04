from machine import Pin
import time

led = Pin(5, Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)