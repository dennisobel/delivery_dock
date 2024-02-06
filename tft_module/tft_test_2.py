import time
from PIL import Image, ImageDraw, ImageFont
import st7735

# Create ST7735 LCD display class
disp = st7735.ST7735(
    port=0,
    cs=st7735.BG_SPI_CS_FRONT,
    dc="PIN21",
    backlight="PIN32",
    rotation=90,
    spi_speed_hz=4000000
)

# Initialize display
disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

# Function to display message and wait for input
def display_prompt(prompt):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    draw.text((10, 10), prompt, font=font, fill=(255, 255, 255))
    disp.display(img)

# Welcome screen
display_prompt("Welcome! Enter locker number:")
time.sleep(2)

# Capture locker number
locker_number = input("Enter locker number: ")

# Prompt for password
display_prompt("Enter password:")
time.sleep(2)

# Capture password
password = input("Enter password: ")

# Compare password
correct_password = "1234"  # Change this to your desired password
if password == correct_password:
    display_prompt("Locker unlocked!")
else:
    display_prompt("Wrong password. Try again.")
