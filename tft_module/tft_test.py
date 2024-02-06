import board #uninstall if not working
import digitalio 
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7735 as st7735

# Configuration for the TFT display
spi = board.SPI()
tft_cs = digitalio.DigitalInOut(board.CE0)
tft_dc = digitalio.DigitalInOut(board.D25)
tft_reset = digitalio.DigitalInOut(board.D24)
display = st7735.ST7735R(spi, rotation=90, cs=tft_cs, dc=tft_dc, rst=tft_reset)

# Create a new PIL image with the same dimensions as the display
image = Image.new("RGB", (display.width, display.height), (0, 0, 0))
draw = ImageDraw.Draw(image)

# Draw a border
border_color = (255, 255, 255)  # White color
border_thickness = 4
draw.rectangle(
    (border_thickness, border_thickness, display.width - border_thickness - 1, display.height - border_thickness - 1),
    outline=border_color
)

# Write "TFT" text
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
text = "TFT"
text_width, text_height = draw.textsize(text, font=font)
text_position = ((display.width - text_width) // 2, (display.height - text_height) // 2)
draw.text(text_position, text, fill=(255, 255, 255), font=font)

# Display the image on the TFT screen
display.image(image)
