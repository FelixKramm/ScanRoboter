from distance import *
from motor_controll import *
from rotation_sensor import *

motor_init()
gyro_init()

time.sleep(10)
#forward(3)
time.sleep(5)
spin(360)
