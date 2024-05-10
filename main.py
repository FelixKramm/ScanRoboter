from distance import *
from motor_controll import *
from rotation_sensor import *
from plotter import *
from random import random
from servo import *
from write_csv import *
import math

global ego_pos
global object_pos

runs = 0
ego_pos = [[0,0]]
object_pos = []
motor_init()

while runs <= 5:
	objects_pos_per_runs = get_obj_position(ego_pos[-1])
	for tupel in objects_pos_per_runs:
		object_pos.append(tupel)
	print("Ego Positionen")
	print(ego_pos)
	print("Globale Positionen:")
	print(object_pos)
	
	ego_pos_now = ego_pos[-1]
	forward_meter(0.4)
	motor_init()
	
	ego_pos_new = [ego_pos_now[0], ego_pos_now[1]+0.4]
	ego_pos.append(ego_pos_new)
	runs += 1

print("Done")
write_ego(ego_pos)
write_row(1,object_pos)



