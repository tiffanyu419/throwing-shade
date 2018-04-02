"""
This is a library of functions for initialization of the shades
"""
import control_shades

# function to manually initialize the shades
def initialization():
	print"To initialize first roll shades all the way up"
	control_shades.initialize_up()
	count = control_shades.initialize_down()
	return count

# function to input a known window length and state of shade
def predetermined_init():
	total_steps = raw_input("Put in the total number of steps to roll up shades: ")
	cur_state = raw_input("Put in the current state of shade: ")
	return (int(total_steps), int(cur_state))
	
