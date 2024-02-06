import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Define keypad button pins
ROW_PINS = [6, 13, 19, 26]
COL_PINS = [16, 20, 21]
admin_password="1234"

# Set up buttons as inputs
for pin in ROW_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set row pins as pulled up inputs
for pin in COL_PINS:
    GPIO.setup(pin, GPIO.OUT)  # set column pins as outputs




# Function to read key input
def read_key():
    for col_pin in COL_PINS:
        # write all column pins high
        for all_pins in COL_PINS:
            GPIO.output(all_pins, GPIO.HIGH)

        GPIO.output(col_pin, GPIO.LOW)

        for row_pin in ROW_PINS:
            if not GPIO.input(row_pin):
                button_index = (col_pin, row_pin)

                if col_pin == COL_PINS[0]:
                    if row_pin == ROW_PINS[0]:
                        return '1'
                    elif row_pin == ROW_PINS[1]:
                        return '4'
                    elif row_pin == ROW_PINS[2]:
                        return '7'
                    elif row_pin == ROW_PINS[3]:
                        return '*'
                elif col_pin == COL_PINS[1]:
                    if row_pin == ROW_PINS[0]:
                        return '2'
                    elif row_pin == ROW_PINS[1]:
                        return '5'
                    elif row_pin == ROW_PINS[2]:
                        return '8'
                    elif row_pin == ROW_PINS[3]:
                        return '0'
                elif col_pin == COL_PINS[2]:
                    if row_pin == ROW_PINS[0]:
                        return '3'
                    elif row_pin == ROW_PINS[1]:
                        return '6'
                    elif row_pin == ROW_PINS[2]:
                        return '9'
                    elif row_pin == ROW_PINS[3]:
                        return '#'

    return None
# Function to read keypad input
def read_keypad():
    try:
        
        previous_time = time.time()
        debounce=0.1
        input_buffer=[]
        while True:
            key = read_key()
            if key is not None:
                current_time = time.time()
                time_elapsed = current_time - previous_time
                previous_time = current_time
                if time_elapsed>debounce: 
                    print(f"{key}", end="")
                    if key=='#':
                        return ''.join(input_buffer)
                    input_buffer.append(key)         
                    
                    #print("Press a key...")
            time.sleep(0.2)

    except KeyboardInterrupt:
        GPIO.cleanup()
try:
    print("enter number ...")
    value=read_keypad()
    print(f"You have entered:{value}")
    if value==admin_password:
        print("correct password")
    else:
        print("wrong password!")
except KeyboardInterrupt:
    GPIO.cleanup()

