from time import sleep

import serial

PORT = "rfc2217://localhost:4000"
ser = serial.serial_for_url(PORT, baudrate=115200, timeout=2)


def send(command):
    """Send one command and return the target's reply."""
    ser.write((command + "\n").encode())
    reply = ser.readline()
    if not reply:
        raise TimeoutError(f"No reply received for command: {command!r}")
    return reply.decode().strip()


if __name__ == "__main__":
    print(send("LED ON"))
    sleep(1)

    print(send("LED OFF"))
    sleep(1)

    print(send("HELLO"))
