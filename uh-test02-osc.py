#!/usr/bin/python3
#
# uh-test02-osc.py - simple OSC server for Unicorn HAT
#
# Unicorn HAT
#   http://shop.pimoroni.com/products/unicorn-hat
#   https://github.com/pimoroni/UnicornHat
#
# setup
#   $ sudo -i
#   # \curl -sS get.pimoroni.com/unicornhat | bash
#   # exit
#   $ sudo pip-3.2 install python-osc
#
import unicornhat as uh
from time      import sleep
from pythonosc import dispatcher
from pythonosc import osc_server

def set_brightness(addr, b):
  print("set_brightness() : b={0}".format(b))
  uh.brightness(b)
  uh.show()

def set_clear(addr):
  print("set_clear()")
  set_color(None, 0, 0, 0)

def set_color(addr, r, g, b):
  print("set_color() : r={0}, g={1}, b={2}".format(r, g, b))
  for y in range(8):
    for x in range(8):
      uh.set_pixel(x, y, r, g, b)
  uh.show()

def set_flash(addr, t, r, g, b):
  print("set_flash() : t={0}, r={1}, g={2}, b={3}".format(t, r, g, b))
  set_color(None, 255, 255, 255)
  sleep(t)
  set_clear(None)

if __name__ == "__main__":
  uh.brightness(.2)
  set_clear(None)

  dispatcher = dispatcher.Dispatcher()

  dispatcher.map("/debug", print)
  dispatcher.map("/brightness", set_brightness)
  dispatcher.map("/clear",      set_clear)
  dispatcher.map("/color",      set_color)
  dispatcher.map("/flash",      set_flash)
  #dispatcher.map("/pixel",      set_pixel)

  server = osc_server.ThreadingOSCUDPServer(
      ("0.0.0.0", 7000), dispatcher)
  print("Unicorn HAT OSC Server on {}".format(server.server_address))
  server.serve_forever()
