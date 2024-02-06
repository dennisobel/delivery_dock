# keypad_module.py
import time
import RPi.GPIO as GPIO
from pad4pi import rpi_gpio

def setup_keypad(row_pins, col_pins):
    GPIO.setmode(GPIO.BCM)
    KEYPAD = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ["*", 0, "#"]
    ]

    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_keypad(keypad=KEYPAD, row_pins=row_pins, col_pins=col_pins)

    return keypad

def capture_input(keypad, process_slot_func, process_password_func):
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        GPIO.cleanup()
