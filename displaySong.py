from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions

def displaySong():
    options = RGBMatrixOptions()
    # Set your RGB matrix options here
    options.rows = 32
    options.cols = 32
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'  # Change to 'adafruit-hat-pwm' if using the Adafruit HAT/PWM
    options.gpio_slowdown = 4
    options.limit_refresh_rate_hz = 30
    options.pwm_bits = 11

    matrix = RGBMatrix(options=options)

    try:
        image = Image.open("images/currentsong.jpg")
        matrix.SetImage(image.convert('RGB'))
        print("Displaying image on the RGB matrix.")
    except IOError:
        print("Error loading image for the RGB matrix.")
