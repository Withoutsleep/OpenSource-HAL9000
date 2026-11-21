from gpiozero import LED
from time import sleep
import json
import limbic_management

led_ojo=LED(17)  #Si cambias esto puedes colocar aquí el GPIO pin que tu quieras 

print("Core loaded")

while True:

    #Led error crítico

    #Led error

    #Led acceso

    #Led escuchando
    if limbic_management.leer_estado("escuchando") == True:
        led_ojo.on()
        sleep(0.2)
        led_ojo.off()
        sleep(0.2)

    #Led normal
    elif led_ojo.on() == False:
        led_ojo.on() #Indica el funcionamiento de Hal
	#Espera para el led normal
        sleep(2)
    sleep(0.5)
