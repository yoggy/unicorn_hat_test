#!/usr/bin/python
#
# uh-test01-speedlight.py - Prototype of LED Speedlite with Unicorn Hat
#
#   Unicorn Hat
#   http://shop.pimoroni.com/products/unicorn-hat
# 
import unicornhat as uh
import time

def set_color(r, g, b):
  for y in range(8):
    for x in range(8):
      uh.set_pixel(x, y, r, g, b)
  uh.show()

uh.brightness(1.0)
while True:
  set_color(255, 255, 255)
  time.sleep(.01)
  set_color(0, 0, 0)
  time.sleep(2.0)
