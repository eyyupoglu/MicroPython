import time
import machine
from machine import DAC,ADC


adc33 = ADC(machine.Pin(sensor_pin))#define sensor pin
adc33.atten(ADC.ATTN_11DB) #define adc
dac26 = DAC(machine.Pin(led_pin))#define DAC
dac26.write(starting_value)#adjust the intensity of the LED
data=[]
sum=0





f = open('data', 'w')
while True:

	for i in range(100):
		time.sleep(0.01)
		sum=sum+adc33.read()
	avg=sum/100
	f.write("%s\n" % avg)
	print("Average of 100 measurements in one second is ",avg)
	sum=0
	avg=0
f.close()
	
