#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
import math
from servo import *
 
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
 
def get_distance():
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
    
    
def get_obj_position(ego):
    offset_sensor_1 = [0.12,0]
    offset_sensor_2 = [-0.12, 0]
    angles_to_check = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]
    #angles_to_check = [90]
    objects_positions = []
    
    for angle in angles_to_check:
        servo_right(angle)
        servo_left(angle)
        [dis_sen1_1, dis_sen2_1] = get_distance()
        [dis_sen1_2, dis_sen2_2] = get_distance()
        [dis_sen1_3, dis_sen2_3] = get_distance()
        dis_sen1 = (dis_sen1_1 + dis_sen1_2 + dis_sen1_3)/3
        dis_sen2 = (dis_sen2_1 + dis_sen2_2 + dis_sen2_3)/3
        if dis_sen1*0.01 <= 3:
            #Sensor 1 - R
            x_sen1 = math.sin(math.radians(angle))*dis_sen1*0.01 + offset_sensor_1[0]+ego[0]
            y_sen1 = math.cos(math.radians(angle))*dis_sen1*0.01 + offset_sensor_1[1]+ego[1]
            objects_positions.append([round(x_sen1,2), round(y_sen1,2)])
        
        if dis_sen2*0.01 <= 3:
            #Sensor 2 - L
            x_sen2 = -1*math.sin(math.radians(angle))*dis_sen2*0.01 + offset_sensor_2[0]+ego[0]
            y_sen2 = math.cos(math.radians(angle))*dis_sen2*0.01 + offset_sensor_2[1]+ego[1]
            objects_positions.append([round(x_sen2,2), round(y_sen2,2)])
            
        time.sleep(0.25)
    return objects_positions
    
        
        
        
    
 
if __name__ == '__main__':
    try:
        while True:
            abstand = get_distance()
            print ("Entfernung1 = %.1f cm" % abstand[0])
            print ("Entfernung2 = %.1f cm" % abstand[1])
            time.sleep(1)
 
        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()
