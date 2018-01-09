"real test"
import time
import machine
from machine import ADC,PWM


p13 = machine.Pin(13,machine.Pin.OUT)
pwm13 = PWM(p13)
pwm13.freq(500)
adc33 = ADC(machine.Pin(33))
adc33.atten(ADC.ATTN_11DB)



f = open('data', 'w')
for i in range(1,1500):
    time.sleep(0.001)
    pwm13.duty(i)
    f.write("%s\n" % adc33.read())
f.close()





f = open('data', 'w')
for i in range(500,1000,10):
    time.sleep(0.01)
    pwm13.duty(i)
    data.append(adc33.read())
f.write((data))


###########################DAC fade in fade out
import time
import machine
from machine import DAC,ADC



adc33 = ADC(machine.Pin(33))
adc33.atten(ADC.ATTN_11DB) #define adc

dac26 = DAC(machine.Pin(26))
dac26.write(0)
time.sleep(1)

data=[]
f = open('data', 'w')
for i in range(1,255):
    time.sleep(0.1)
    dac26.write(i)
    data.append(adc33.read())
    f.write("%s\n" % adc33.read())
    print(data[i-1])
f.close()

f = open('data', 'r')#open the file for reading purpose
f.read() # then you can read


#############################button start experiment end 
import time
import machine
from machine import DAC,ADC

button_pin=13
sensor_pin=33
led_pin=26
starting_value = 255

def experiment(starting_value, button_pin, sensor_pin, led_pin):
	button = machine.Pin(button_pin, machine.Pin.IN)#define button pin
	adc33 = ADC(machine.Pin(sensor_pin))#define sensor pin
	adc33.atten(ADC.ATTN_11DB) #define adc
	dac26 = DAC(machine.Pin(led_pin))#define DAC
	dac26.write(starting_value)#adjust the intensity of the LED
	data=[]
	i=0
	while True:
		if button.value()==1:
		    f = open('data', 'w')
		    while True:
			    time.sleep(0.1)
			    data.append(adc33.read())
			    f.write("%s\n" % adc33.read())#
			    print(data[i-1])
			    if button.value()==1:
				time.sleep(1)
				break			
			    i=i+1
		    f.close()
		   
	    
experiment(starting_value, button_pin, sensor_pin, led_pin)






































