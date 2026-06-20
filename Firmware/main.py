from machine import Pin, I2S, SPI
from ili9341 import Display, color565
from utime import sleep

#buttons
button1 = Pin(6, Pin.IN, Pin.PULL_UP)
button2 = Pin(7, Pin.IN, Pin.PULL_UP)
button3 = Pin(8, Pin.IN, Pin.PULL_UP)
button4 = Pin(9, Pin.IN, Pin.PULL_UP)

#jotstick
joystick_right = Pin(2, Pin.IN, Pin.PULL_UP)
joystick_left = Pin(3, Pin.IN, Pin.PULL_UP)
joystick_up = Pin(4, Pin.IN, Pin.PULL_UP)
joystick_down = Pin(5, Pin.IN, Pin.PULL_UP)

#amplifier
sd_mode = Pin(19, Pin.OUT)
sd_mode.value(1)
i2s = I2S(0, sck=Pin(16), ws=Pin(17), sd=Pin(18), mode=I2S.TX, bits=16, format=I2S.STEREO, rate=44100, ibuf=40000)

#tft display
spi = SPI(1, baudrate=40_000_000, sck=Pin(10), mosi=Pin(11))
display = Display(spi, cs=Pin(13), dc=Pin(14), rst=Pin(15))

white = color565(255, 255, 255)
black = color565(0, 0, 0)
green = color565(0, 255, 0)

display.clear()
display.draw_text8x8(10, 10, "Arcade Panel", white)

def display_write_line(y, text):
    display.fill_rectangle(10, y, 220, 8, black)
    display.draw_text8x8(10, y, text, green)

def play_music(filename, stop_button):
    while True:
        with open(filename, "rb") as f:
            f.seek(44)
            while True:
                data = f.read(2048)
                if not data:
                    break
                if stop_button.value() == 0:
                    while stop_button.value() == 0: #wait until button is released
                        sleep(0.01)
                    return
                i2s.write(data)

last_button1 = 1
switch = False
counter = 0

while True:
    current = button1.value()

    if current == 0 and last_button1 == 1:
        display_write_line(40, "Playing music...")
        play_music("retromsuic.wav", button1)
        display_write_line(40, "Music was stopped")
    last_button1 = current
        
    if button2.value() == 0:
        display_write_line(40, "This button does nothing but counting")
        counter += 1
        display_write_line(20, f"{counter}")

    elif button3.value() == 0:
        print("BUTTON1")
    elif button4.value() == 0:
        print("BUTTON2")
    
    if joystick_right.value() == 0:
        print("RIGHT")
    elif joystick_left.value() == 0:
        print("LEFT")
    elif joystick_up.value() == 0:
        print("UP")
    elif joystick_down.value() == 0:
        print("DOWN")   
    sleep(0.05)

