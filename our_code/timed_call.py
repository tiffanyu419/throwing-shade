"""
This is a library that contains the implementation of an alarm clock
that would control the state of the shades
"""
from control_shades import move_up, move_down
import time

def control(cur_state, init_state):
	print "If you want to set wake up time, please type 'w'"
	print "If you want to set sleep time, please type 's'"
	print "If you want to quit, please type 'q'"
	command = raw_input(">> ")
	if command == 'w':
		cur_state = morning(cur_state, init_state)
	elif command == 's':
		cur_state = night(cur_state, init_state)
	elif command == 'q':
		return cur_state
	else:
		print "Invalid input"

def morning(cur_state, init_state):
	wake_up = raw_input("Please enter your wake up time in military time: ")
	local_time = time.localtime(time.time())
	hour = int(wake_up[:2])
	minutes = int(wake_up[2:])
	print "Current time: %d : %d : %d" %(local_time.tm_hour, local_time.tm_min, local_time.tm_sec)
	print "Wake up time: %d : %d : 00" %(hour, minutes)
	hour_diff = hour - local_time.tm_hour
	if hour_diff < 0:
		hour_diff += 23
	min_diff = minutes - local_time.tm_min - 1
	if min_diff == 0:
		hour_diff += 1
	elif min_diff < 0:
		min_diff += 60
	sec_diff = 60 - local_time.tm_sec
	total = hour_diff*60*60*60+min_diff*60+sec_diff
	print "Time till wake up: %d secs" %total
	time.sleep(total)
	move_up(cur_state)
	print "Wake up!"
	return 0

def night(cur_state, init_state):
	wake_up = raw_input("Please enter your sleep time in military time: ")
	local_time = time.localtime(time.time())
	hour = int(wake_up[:2])
	minutes = int(wake_up[2:])
	print "Current time: %d : %d : %d" %(local_time.tm_hour, local_time.tm_min, local_time.tm_sec)
	print "Sleep time: %d : %d : 00" %(hour, minutes)
	hour_diff = hour - local_time.tm_hour
	min_diff = minutes - local_time.tm_min - 1
	sec_diff = 60 - local_time.tm_sec
	total = hour_diff*60*60*60+min_diff*60+sec_diff
	print "Rolling down shades in %d secs" %total
	time.sleep(total)
	move_down = (cur_state, init_state)
	print "Goodnight!"
	return init_state
