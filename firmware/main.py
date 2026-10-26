from machine import Pin

led = Pin(15, Pin.OUT)

while True:
    line = input().strip()

    if line == "LED ON":
        led.value(1)
        print("OK")
    elif line == "LED OFF":
        led.value(0)
        print("OK")
    else:
        print("ERR unknown command")