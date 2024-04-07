import smbus
import math
import time
import csv
from gyro import *

# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c


def gyro_init():
	bus = smbus.SMBus(1)  # bus = smbus.SMBus(0) fuer Revision 1
	address = 0x68  # via i2cdetect
	# Aktivieren, um das Modul ansprechen zu koennen
	bus.write_byte_data(address, power_mgmt_1, 0)
	
def get_rotation_angle(angle, step):
	# open the file in the write mode
	f = open('rotation_data.csv', 'w')
	# create the csv writer
	writer = csv.writer(f)
	
	# Calulate the angle with discrete integration
	rotation = 0
	while rotation <= angle:
		gyroskop_zout = read_word_2c(0x47) / 131
		writer.writerow([time.time(),gyroskop_zout])
		rotation += gyroskop_zout * step
		time.sleep(step)
	
	return rotation
	


