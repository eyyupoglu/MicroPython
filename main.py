import time
import machine
from machine import DAC,ADC
import neopixel
from experiment import *
from count_time import *
from color import *
############################################################
red=32
blue=27
green=12
#32:red
#12:green
#27:blue

button_pin=13
sensor_pin=33
led_pin=26
starting_value = 235


###########################################################STARTING#################################################
	    
experiment(starting_value, button_pin, sensor_pin, led_pin, blue, red, green)








