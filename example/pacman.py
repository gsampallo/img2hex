#from time import sleep_ms, ticks_ms,time
import time
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)
lcd.backlight_on()
lcd.clear()


pacman = bytearray([0x4,0xe,0x1b,0x1f,0x18,0x1c,0xf,0xe])
lcd.custom_char(0,pacman)

pacman2 = bytearray([0x4,0xe,0x1b,0x1f,0x3,0x7,0x1e,0xe])
lcd.custom_char(3,pacman2)
lcd.putchar(chr(0))

pastilla = bytearray([0x0,0x0,0x0,0x6,0x6,0x0,0x0,0x0])
lcd.custom_char(1,pastilla)
for item in range(0,15):
    lcd.putchar(chr(1))

fantasma = bytearray([0x4,0xe,0xe,0xe,0xe,0x1e,0x1f,0xe])
lcd.custom_char(2,fantasma)

while True:
    lcd.move_to(0,0)
    for item in range(0,15):
        lcd.putchar(chr(1))    
    i = 0
    while(i < 16):
        
        j=0
        while(j<i):
            lcd.move_to(j,0)
            lcd.putstr(" ")
            j = j + 1

        lcd.move_to(i,0)
        lcd.putchar(chr(0))
        i = i + 1
        time.sleep_ms(400)

    i = i - 2
    while (i > 0):
        j=i
        while(j<16):
            lcd.move_to(j,0)
            lcd.putstr(" ")
            j = j + 1

        lcd.move_to(i,0)
        lcd.putchar(chr(3))
        lcd.putstr(" ") 
        lcd.putchar(chr(2))
        i = i - 1
        time.sleep_ms(350)