#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
 
#GPIO Modus (BOARD / BCM)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
 
#GPIO Pins zuweisen
GPIO_TRIGGER_1 = 12
GPIO_ECHO_1 = 16

GPIO_TRIGGER_2 = 21
GPIO_ECHO_2 = 20
 
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER_1, GPIO.OUT)
GPIO.setup(GPIO_ECHO_1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_2, GPIO.IN)
 
def distanz():
    distanz = [0, 0]
    ### Sensor 1 ###
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER_1, True)
 
    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_1, False)
 
    StartZeit = time.time()
    StopZeit = time.time()
 
    # speichere Startzeit_1
    while GPIO.input(GPIO_ECHO_1) == 0:
        StartZeit_1 = time.time()
 
    # speichere Ankunftszeit_2
    while GPIO.input(GPIO_ECHO_1) == 1:
        StopZeit_1 = time.time()
 
    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit_1 - StartZeit_1
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz[0] = (TimeElapsed * 34300) / 2
    
    ### Sensor 2 ###
    GPIO.output(GPIO_TRIGGER_2, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_2, False)
    StartZeit = time.time()
    StopZeit = time.time()
    
    # speichere Startzeit_2
    while GPIO.input(GPIO_ECHO_2) == 0:
        StartZeit_2 = time.time()
 
    # speichere Ankunftszeit_2
    while GPIO.input(GPIO_ECHO_2) == 1:
        StopZeit_2 = time.time()
 
    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit_2 - StartZeit_2
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz[1] = (TimeElapsed * 34300) / 2
 
    return distanz
 
if __name__ == '__main__':
    try:
        while True:
            abstand = distanz()
            print ("Entfernung1 = %.1f cm" % abstand[0])
            print ("Entfernung2 = %.1f cm" % abstand[1])
            time.sleep(1)
 
        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
