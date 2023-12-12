import time
import RPi.GPIO as GPIO
from time import sleep
from rotation_sensor import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

### Definition Pinout und Aufstartverhalten
powerlevel = 100

#Motor 1
in1 = 15
in2 = 18
enA = 14
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p1=GPIO.PWM(enA,1000)

#Motor 2
in3 = 23
in4 = 24
enB = 25
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p2=GPIO.PWM(enB,1000)

p1.start(powerlevel)
p2.start(powerlevel)

# open the file in the write mode
f = open('rotation_data.csv', 'w')
# create the csv writer
writer = csv.writer(f)
	



### Funktionsdefinition

def motor_init():
	p1.start(powerlevel)
	p2.start(powerlevel)
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
	
def forward(seconds):
	p1.start(75)
	p2.start(75)
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in4,GPIO.HIGH)
	GPIO.output(in3,GPIO.LOW)
	time.sleep(seconds)
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)

def backward(seconds):
	p1.start(75)
	p2.start(75)
	GPIO.output(in2,GPIO.HIGH)
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in3,GPIO.HIGH)
	GPIO.output(in4,GPIO.LOW)
	time.sleep(seconds)
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)

def spin(angle):
	p1.start(85)
	p2.start(85)
	GPIO.output(in1,GPIO.HIGH)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.HIGH)
	GPIO.output(in4,GPIO.LOW)
	angle_out = get_rotation_angle(angle, 0.05)
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
	writer.writerow(["Rotation aim",angle,"messured Angle",angle_out])
	
def spin_reverse(seconds):
	p1.start(80)
	p2.start(80)
	GPIO.output(in2,GPIO.HIGH)
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in4,GPIO.HIGH)
	GPIO.output(in3,GPIO.LOW)
	time.sleep(seconds)
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)






### Start Test ###
#time.sleep(15)

#Test run Forward
#p1.start(75)
#p2.start(75)
#GPIO.output(in1,GPIO.HIGH)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in4,GPIO.HIGH)
#GPIO.output(in3,GPIO.LOW)
#time.sleep(2)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.LOW)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(1)

#Test run backward
#p1.start(75)
#p2.start(75)
#GPIO.output(in2,GPIO.HIGH)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in3,GPIO.HIGH)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(2)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.LOW)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(10)

#Test run spin
#p1.start(80)
#p2.start(80)
#GPIO.output(in1,GPIO.HIGH)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.HIGH)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(3+0.2)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.LOW)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(10)

#Test run spin reverse
#p1.start(80)
#p2.start(80)
#GPIO.output(in2,GPIO.HIGH)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in4,GPIO.HIGH)
#GPIO.output(in3,GPIO.LOW)
#time.sleep(3+0.2)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.LOW)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(10)

#Test run spin 90°
#p1.start(80)
#p2.start(80)
#GPIO.output(in1,GPIO.HIGH)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.HIGH)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(0.75+0.2)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.LOW)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(10)

#Test run spin 180°
#p1.start(80)
#p2.start(80)
#GPIO.output(in1,GPIO.HIGH)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.HIGH)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(1.5+0.2)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.LOW)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(10)

#Test run spin 45°
#p1.start(80)
#p2.start(80)
#GPIO.output(in1,GPIO.HIGH)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.HIGH)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(0.375+0.2)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.LOW)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(10)

#Test run spin 360°
#p1.start(80)
#p2.start(80)
#GPIO.output(in2,GPIO.HIGH)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in4,GPIO.HIGH)
#GPIO.output(in3,GPIO.LOW)
#time.sleep(3+0.2)
#GPIO.output(in1,GPIO.LOW)
#GPIO.output(in2,GPIO.LOW)
#GPIO.output(in3,GPIO.LOW)
#GPIO.output(in4,GPIO.LOW)
#time.sleep(1)
