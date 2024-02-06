# password_module.py

def process_password(key, entered_password):
    if key == "#":
        print("Access granted." if entered_password[0] == "1234" else "Access denied.")
        entered_password[0] = ""  # Reset entered password
    elif key == "*":
        entered_password[0] = ""  # Reset entered password
        print("Password reset.")
    else:
        entered_password[0] += str(key)
        print(f"Entered password: {entered_password[0]}")
