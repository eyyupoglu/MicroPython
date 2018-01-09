http://172.20.10.13/
ap.config(essid='Group20(ESP1A0981)', authmode=network.AUTH_WPA_WPA2_PSK, password='micropythoN');


import machine
import json
#Imports the socket, which allows us to creat a server. 
import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

#Creats a socket that will listen for clients. 
s = socket.socket()
s.bind(addr)
s.listen(1)



#############################MicroPython v1.8.6-7-gefd0927 on 2016-11-10; ESP module with ESP8266
Type "help()" for more information.
>>> import network;
>>> ap = network.WLAN(network.AP_IF);
>>> ap.active(True);
>>> ap.config(essid='MyESP8266', authmode=network.AUTH_WPA_WPA2_PSK, password='mypassword');
>>> print(ap.config('essid'));
MyESP8266
>>> 
