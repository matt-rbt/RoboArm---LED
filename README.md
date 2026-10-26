# RoboArm LED Host-Target Tutorial

This project shows the host-target pattern used in the RoboArm workshop: the Pico handles real-time GPIO work while the laptop sends simple text commands over serial.

## What this tutorial does

- The Pico runs MicroPython and listens for serial commands.
- The host laptop sends commands such as `LED ON` and `LED OFF`.
- The Pico replies with `OK` or `ERR unknown command`.

This is the same pattern you will reuse later for motor control.


## Start the Wokwi simulator

1. Open the project in VS Code.
2. Open the Wokwi simulation tab.
3. Keep the simulator visible while the host script is running.
4. Load the project with the configured Pico board and LED.

The simulator is configured to expose the serial port on:

```text
rfc2217://localhost:4000
```

## Target code

The Pico firmware is stored in `main.py`:

```python
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
```
run it with 

```sh
python -m mpremote connect port:rfc2217://localhost:4000 run firmware/main.py
```

## Host code

The laptop-side script is `host.py`:

```python
import serial

PORT = "rfc2217://localhost:4000"
ser = serial.serial_for_url(PORT, baudrate=115200, timeout=2)


def send(command):
    ser.write((command + "\n").encode())
    return ser.readline().decode().strip()


print(send("LED ON"))
print(send("LED OFF"))
print(send("HELLO"))
```

## Run the example

1. Start the Pico program inside Wokwi.
2. In a terminal at the project root, run:

```bash
python3 host.py
```

Expected output:

```text
OK
OK
ERR unknown command
```

The LED in the simulator should turn on and off as commands are sent.

## Troubleshooting

- If the script hangs, the Wokwi simulator tab may be hidden or paused.
- If serial connection fails, check that the Wokwi server is running on port 4000.
- If the LED does not respond, verify that the Pico is connected to GP15 in the Wokwi diagram.
- If `pyserial` is missing, run `python3 -m pip install -r requirements.txt`.

## Next step

This LED example is the first building block for the motor control assignment. The same communication pattern is reused, but the host script calculates movement and the Pico just executes the command and reports status.

