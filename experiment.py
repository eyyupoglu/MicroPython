import time
import machine
from machine import DAC,ADC
import neopixel
from count_time import *
from color import *



def create_data_file(starting_value, button_pin, sensor_pin, led_pin, blue, red, green,counter):
    button = machine.Pin(button_pin, machine.Pin.IN)#define button pin
    adc33 = ADC(machine.Pin(sensor_pin))#define sensor pin
    adc33.atten(ADC.ATTN_11DB) #define adc
    dac26 = DAC(machine.Pin(led_pin))#define DAC
    dac26.write(starting_value)#adjust the intensity of the LED
    data=[]
    i=0
    f = open('data'+str(counter), 'w')
    while True:
	    time.sleep(0.1)
	    data.append(adc33.read())
	    f.write("%s\n" % adc33.read())#
	    print(data[i-1])
	    if button.value()==1:#button is pressed again
		color("blue", blue, red, green)
		time.sleep(1)
		break			
	    i=i+1
    f.close()
def experiment(starting_value, button_pin, sensor_pin, led_pin, blue, red, green):
	button = machine.Pin(button_pin, machine.Pin.IN)#define button pin
	adc33 = ADC(machine.Pin(sensor_pin))#define sensor pin
	adc33.atten(ADC.ATTN_11DB) #define adc
	dac26 = DAC(machine.Pin(led_pin))#define DAC
	dac26.write(starting_value)#adjust the intensity of the LED
	data=[]
	i=0
	counter=0
	while not count_time(button_pin) :
		print("here!!")
		if button.value()==1:
		    color("green", blue, red, green)#if the experiment runs neopixel gives green color
		    if counter<5:
			create_data_file(starting_value, button_pin, sensor_pin, led_pin, blue, red, green, counter)#create new data file
			counter += 1
		    color("purple", blue, red, green)
	
	color("white", blue, red, green)	   
	time.sleep(5)
	color("no", blue, red, green)
