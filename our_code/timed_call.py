"""
This is a library that contains the implementation of an alarm clock
that would control the state of the shades
"""
from control_shades import allUp, allDown
import time

def control(cur_state, init_state):
	print "Setting up your wake up and sleep time!"
	time_up = morning(cur_state, init_state)
	print "%d secs till wake up" %time_up
	time_down = night(cur_state, init_state)
	print "%d secs till sleep" %time_down
	if time_up < time_down:
		diff = time_down - time_up
		sleep(time_up)
		allUp(cur_state, 0)
		sleep(diff)
		allDown(0, init_state)
	else:
		diff = time_up - time_down
		sleep(time_down)
		allDown(cur_state, init_state)
		sleep(diff)
		allUp(init_state, 0)

def calc_time_diff(time):
	hour = int(time[:2])
	minutes = int(time[2:])
	local_time = time.localtime(time.time())
	print "Current time: %d : %d : %d" %(local_time.tm_hour, local_time.tm_min, local_time.tm_sec)
	hour_diff = hour - local_time.tm_hour
	if hour_diff < 0:
		hour_diff += 24
	min_diff = minutes - local_time.tm_min - 1
	if min_diff == 0:
		hour_diff -= 1
	if min_diff < 0:
		min_diff += 60
	sec_diff = 60 - local_time.tm_sec
	if sec_diff == 0:
		min_diff -= 1
	if sec_diff < 0:
		sec_diff += 60
	total = hour_diff*60*60+min_diff*60+sec_diff

	return total

def morning(cur_state, init_state):
	input_time = raw_input("Please enter your wake up time in military time: ")
	return calc_time_diff(input_time)

def night(cur_state, init_state):
	input_time = raw_input("Please enter your sleep time in military time: ")
	return calc_time_diff(input_time)
