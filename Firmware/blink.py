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
sd_mode = Pin(19, Pin.OUT, Pin.PULL_UP)
i2s = I2S(0, sck=Pin(16), ws=Pin(17), sd=Pin(18), mode=I2S.TX, bits=16, format=I2S.STEREO, rate=44100, ibuf=40000)

#tft display
spi = SPI(0, baudrate=40_000_000, sck=Pin(10), mosi=Pin(11))
display = Display(spi, cs=Pin(13), dc=Pin(14), rst=Pin(15))

while True:
    if button1.value() == 0:
        ...
    elif button2.value() == 0:
        ...
    elif button3.value() == 0:
        ...
    elif button4.value() == 0:
        ...
    
    if joystick_right.value() == 0:
        ...
    elif joystick_left.value() == 0:
        ...
    elif joystick_up.value() == 0:
        ...
    elif joystick_down.value() == 0:
        ...

