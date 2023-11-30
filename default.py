from PIL import Image, ImageOps
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # Change to 'adafruit-hat-pwm' if using the Adafruit HAT/PWM
options.gpio_slowdown = 4
options.limit_refresh_rate_hz = 60
options.pwm_bits = 11
options.pwm_lsb_nanoseconds = 100
options.pwm_dither_bits = 2
options.brightness = 100

matrix = RGBMatrix(options=options)

# Load the image
image = Image.open("images/default.png")

# Resize the image with LANCZOS (antialiasing)
matrix_size = (options.cols * options.chain_length, options.rows)
image = ImageOps.fit(image, matrix_size, Image.Resampling.LANCZOS)

# Display the image
matrix.SetImage(image.convert('RGB'))

# Keep the image displayed for a duration
time.sleep(900)
