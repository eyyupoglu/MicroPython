import time
import machine
from machine import DAC,ADC
import neopixel


def color(color,blue_pin, red_pin, green_pin):
	red_light = machine.Pin(red_pin,machine.Pin.OUT)
	blue_light = machine.Pin(blue_pin,machine.Pin.OUT)
	green_light = machine.Pin(green_pin,machine.Pin.OUT)
	if color == "red":
		green_light.value(1)
		blue_light.value(1)
		red_light.value(0)
	elif color == "green":
		green_light.value(0)
		blue_light.value(1)
		red_light.value(1)
	elif color == "blue":
		green_light.value(1)
		blue_light.value(0)
		red_light.value(1)
	elif color == "yellow":
		green_light.value(0)
		blue_light.value(1)
		red_light.value(0)
	elif color == "turquoise":
		green_light.value(0)
		blue_light.value(0)
		red_light.value(1)
	elif color == "purple":
		green_light.value(1)
		blue_light.value(0)
		red_light.value(0)
	elif color == "white":
		green_light.value(0)
		blue_light.value(0)
		red_light.value(0)
	elif color == "no":
		green_light.value(1)
		blue_light.value(1)
		red_light.value(1)


