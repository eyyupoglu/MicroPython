import time
import machine
from machine import DAC,ADC
import neopixel


def count_time(button_pin):
	button = machine.Pin(button_pin, machine.Pin.IN)#define button pin
	delay=0
	while button.value()==1:
		delay=delay+1
		time.sleep(1)
	if delay>1:
		return True
	else :
		return False

