
import time
import machine
from machine import DAC,ADC
import neopixel
from count_time import *
from color import *



def create_data_file(starting_value, button_pin, sensor_pin, led_pin, blue, red, green,counter):
    button = machine.Pin(button_pin, machine.Pin.IN)#define button pin
    adc33 = ADC(machine.Pin(sensor_pin))#define sensor pin
    adc33.atten(ADC.ATTN_6DB) #define adc
    dac26 = DAC(machine.Pin(led_pin))#define DAC
    dac26.write(starting_value)#adjust the intensity of the LED
    data=[]
    i=0
    f = open('data'+str(counter), 'w')
    while True:
	    #Take the average of the measurments every 1,2 seconds
	    sum = 0
	    for i in range(120):
	        if button.value() == 1 :
		    break
	        sum = sum + adc33.read()
	        time.sleep(0.01)
	    average = sum/120
	    data.append(average)
	    f.write("%s\n" % average)
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
	adc33.atten(ADC.ATTN_6DB) #define adc
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

	#Take the average of the measurments every 1,2 seconds
	sum = 0
	for i in range(120):
	    if button.value() == 1 :
		break
            sum = sum + adc33.read()
            time.sleep(0.01)
        average = sum/12000	
