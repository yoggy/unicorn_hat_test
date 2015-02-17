#!/usr/bin/python3
#
# uh-test02-osc.py - simple OSC server for Unicorn HAT
#
# Unicorn HAT
#     http://shop.pimoroni.com/products/unicorn-hat
#     https://github.com/pimoroni/UnicornHat
#
# setup
#     $ sudo -i
#     # \curl -sS get.pimoroni.com/unicornhat | bash
#     # exit
#     $ sudo pip-3.2 install python-osc
#
import unicornhat as uh
from time      import sleep
from pythonosc import dispatcher
from pythonosc import osc_server

def set_brightness(b):
  uh.brightness(b)
  uh.show()

def set_color(r, g, b):
  for y in range(8):
    for x in range(8):
      uh.set_pixel(x, y, r, g, b)
  uh.show()

#
# /brightness handler
#
# args
#     float brightness (0.0-1.0)
# ex.
#     $ sendosc 192.168.1.100 7000 /brightness f 0.3
#
def handle_brightness(addr, b):
  print("/brightness : addr={0}, b={1}".format(addr, b))
  set_brightness(b)

#
# /clear handler
#
# args
#     None
# ex.
#     $ sendosc 192.168.1.100 7000 /clear 
#
def handle_clear(addr):
  print("/clear : addr={0}".format(addr))
  set_color(0, 0, 0)

#
# /color handler
# 
# args
#     int   red   (0-255)
#     int   green (0-255)
#     int   blue  (0-255)
#
# ex.
#     $ sendosc 192.168.1.100 7000 /color i 255 i 255 i 255
#
def handle_color(addr, r, g, b):
  print("/color : addr={0}, r={1}, g={2}, b={3}".format(addr, r, g, b))
  set_color(r, g, b)

#
# /flash handler
# 
# args
#     float time  (sec)
#     int   red   (0-255)
#     int   green (0-255)
#     int   blue  (0-255)
#
# ex.
#     $ sendosc 192.168.1.100 7000 /flash f 0.03 i 255 i 255 i 255
#
def handle_flash(addr, t, r, g, b):
  print("/flash : addr={0}, t={1}, r={2}, g={3}, b={4}".format(addr, t, r, g, b))
  set_color(r, g, b)
  sleep(t)
  set_color(0, 0, 0)

if __name__ == "__main__":
  # startup animation?
  uh.brightness(.2)

  set_color(255, 0, 0)
  sleep(1)
  set_color(255, 255, 0)
  sleep(1)
  set_color(0, 255, 0)
  sleep(2)
  set_color(0, 0, 0)

  dispatcher = dispatcher.Dispatcher()

  dispatcher.map("/brightness", handle_brightness)
  dispatcher.map("/clear",      handle_clear)
  dispatcher.map("/color",      handle_color)
  dispatcher.map("/flash",      handle_flash)

  server = osc_server.ThreadingOSCUDPServer(
      ("0.0.0.0", 7000), dispatcher)
  print("Unicorn HAT OSC Server on {}".format(server.server_address))
  server.serve_forever()
