#######ATTEN##########
import machine
adc = machine.ADC(machine.Pin(39))#pin A3
adc.atten(adc.ATTN_11DB)

import time
while True:
    some_value = adc.read()
    adc.read()
    time.sleep(0.2)
    if some_value <1500 and some_value> 1000:
	led.value(1)
	time.sleep(0.75)
	led.value(0)
	pwm0 = PWM(led)
    elif some_value <1000 and some_value> 750:
	led.value(1)
	time.sleep(0.5)
	led.value(0)
	pwm0 = PWM(led)
    elif some_value <750 and some_value> 500:
	led.value(1)
	time.sleep(0.25)
	led.value(0)
	pwm0 = PWM(led)
    elif some_value <500 and some_value> 250:
	led.value(1)
	time.sleep(0.125)
	led.value(0)
	pwm0 = PWM(led)
    else:
        led.value(1)
	pwm0 = PWM(led)
	

###############led


led = machine.Pin(13, machine.Pin.OUT)
led.value(1)



###########changing light intensity

from machine import Pin, PWM


led = machine.Pin(13, machine.Pin.OUT)
pwm0 = PWM(led)
pwm0.duty(150)



#################button

import machine
button = machine.Pin(13, machine.Pin.IN)



