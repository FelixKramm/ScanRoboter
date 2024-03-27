import RPi.GPIO as GPIO
import time


def servo_left(angle): #connected with dis_sensor2
    servoPIN = 13
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # GPIO als PWM mit 50Hz
    rotate = 2.5 + (10*angle)/180
    p.start(rotate) # Initialisierung
    time.sleep(1)
    
    
def servo_right(angle): #connected with dis_sensor1
    servoPIN = 5
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50) # GPIO als PWM mit 50Hz
    rotate = 12.5 - (10*angle)/180
    p.start(rotate) # Initialisierung
    time.sleep(1)
    
