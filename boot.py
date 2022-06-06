try:
  import usocket as socket
except:
  import socket
from time import sleep_ms
from machine import Pin
import network

import esp

esp.osdebug(True)
 
import gc
gc.collect()
 
blue_pin = Pin(2, Pin.OUT)
green_pin = Pin(0, Pin.OUT)
red_pin = Pin(4, Pin.OUT)

blue_pin_status = False
green_pin_status = False
red_pin_status = False

ssid = 'SSID_WIFI'
password = 'PASSWORD_WIFI'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected():
    sleep_ms(100)
print('Network config:', wlan.ifconfig())

sleep_ms(2000)
