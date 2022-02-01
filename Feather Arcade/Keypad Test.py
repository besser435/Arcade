# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import digitalio
import board
import adafruit_matrixkeypad
import neopixel

# LED pins and setup
led_neo = neopixel.NeoPixel(board.NEOPIXEL, 1)          


# 3x4 matrix keypad - Rows and columns are mixed up for https://www.adafruit.com/product/3845
# Use the same wiring as in the guide with the following setup lines:
cols = [digitalio.DigitalInOut(x) for x in (board.D11, board.D13, board.D9)]
rows = [digitalio.DigitalInOut(x) for x in (board.D12, board.D5, board.D6, board.D10)]

keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

"""while True:
    keys = keypad.pressed_keys
    if keys:
        print("Pressed: ", keys)

    time.sleep(0.1)"""

while True:
    led_neo[0] = (0, 0, 0)
    key = keypad.pressed_keys


    if key == [1]:
        led_neo[0] = (0, 255, 0)

    elif key == [2]:  
        led_neo[0] = (255, 0, 128)     
    
    time.sleep(0.1)
