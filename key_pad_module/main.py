# main.py
from slot_module import process_slot
from password_module import process_password
from keypad_module import setup_keypad, capture_input

def main():
    current_slot = [0]
    entered_password = [""]
    
    def process_key(key):
        process_slot(key, current_slot)
        process_password(key, entered_password)

    ROW_PINS = [5, 6, 13, 19]
    COL_PINS = [12, 16, 20]

    keypad = setup_keypad(ROW_PINS, COL_PINS)

    # Add event listeners
    keypad.registerKeyPressHandler(process_key)

    print("Choose a slot:")
    capture_input(keypad, process_slot, process_password)

if __name__ == "__main__":
    main()
