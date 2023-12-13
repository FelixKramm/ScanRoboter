from distance import *
from motor_controll import *
from rotation_sensor import *
from plotter import *


motor_init()

time.sleep(8)
[time_plot1, gyro_out_plot1, rotation_plot1] = spin(360, 0.2)
#time.sleep(2)
#[time_plot2, gyro_out_plot2, rotation_plot2] = spin(360, 0.05)
#time.sleep(2)
#[time_plot3, gyro_out_plot3, rotation_plot3] = spin(360, 0.02)
#time.sleep(2)
#[time_plot4, gyro_out_plot4, rotation_plot4] = spin(360, 0.01)
plot_rotation(time_plot1, gyro_out_plot1, rotation_plot1)
#plot_rotation(time_plot2, gyro_out_plot2, rotation_plot2)
#plot_rotation(time_plot3, gyro_out_plot3, rotation_plot3)
#plot_rotation(time_plot4, gyro_out_plot4, rotation_plot4)
