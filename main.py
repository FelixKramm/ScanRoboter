from distance import *
from motor_controll import *
from rotation_sensor import *
from plotter import *
from random import random
from servo import *


motor_init()
servo_left(0)
[dis_1, dis_2] = get_distance()
time.sleep(1)
print([dis_2])
servo_right(0)
[dis_1, dis_2] = get_distance()
time.sleep(1)
print([dis_1])
servo_left(180)
[dis_1, dis_2] = get_distance()
time.sleep(1)
print([dis_2])
servo_right(180)
[dis_1, dis_2] = get_distance()
print([dis_1])

	






#time.sleep(2)
#[time_plot1, gyro_out_plot1, rotation_plot1, x, y, z] = spin(720)

#[dis_1, dis_2] = get_distance()
#print([dis_1, dis_2])


#plot_rotation(time_plot1, gyro_out_plot1, rotation_plot1, x,y,z)


