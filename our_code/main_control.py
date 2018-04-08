"""
This is the main interface for the shades, calls on different libraries
and functions to control shades.
"""
import control_shades
import initialization
import timed_call
import time

def main():
	print"Welcome to our shady interface!"
	initialized = False
	end = False
	cur_state = 0
	init_state = 0
	while end == False:
		print"To manually control the shade, please type 'm'"
		print"To initialize the shades, please type 'i'"
		print"To put in predetermined shade length and current state, please type 'k'"
		print"To set a time for the shade to move, please type 't'"
		print"To quit out of the program, please type 'q'"
		command = raw_input(">> ")
		if command == 'm':
			cur_state = control_shades.test_shades(cur_state, init_state)
		elif command == 'i':
			init_state = initialization.initialization()
			cur_state = init_state
			initialized = True
			print"Total steps: %d" %init_state
		elif command == 't':
			if initialized == False:
				print"Please initialize or input states first"
			else:
				cur_state = timed_call.control(cur_state, init_state)
		elif command == 'k':
			init_state, cur_state = initialization.predetermined_init()
			initialized = True
			print "Total steps: %d" %init_state
		elif command == 'q':
			end = True
		else:
			print "Invalid command"
		print "Current State: %d" %cur_state
		
main()
