"""
This is a library that houses functions that directly move the shades
up and down

"""
#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_StepperMotor
import time
import atexit
#import curses

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


# function to move shades 100 steps at a time
##def test_shades(cur_state, init_state):
##    atexit.register(turnOffMotors)
##    myStepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
##    myStepper.setSpeed(80)             # 30 RPM
##    stop = False
##    while stop == False:
##        print("Please use arrow keys to indicate direction and press enter to move the shade. Press return to main menu")
##        c = raw_input(">> ")
##        if c == "":
##            c = prev
##        if c == '\x1b[A':
##            prev = '\x1b[A'
##            myStepper.step(100, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.MICROSTEP)
##            if cur_state >= 100:
##                cur_state -= 100
##	    else:
##                print "Shades are fully rolled up"
##        elif c =='\x1b[B':
##		prev = '\x1b[B'
##		myStepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)
##		if cur_state <= (init_state - 100):
##                    cur_state += 100
##		else:
##				print "Shades are fully extended"
##        elif c == "q":
##            print("Goodbye!")
##            stop = True
##        else:
##            print("Invalid Command")
##    return cur_state

# function to roll the shades down to count number of steps to completely roll down shades
def initialize_down():
	atexit.register(turnOffMotors)
	myStepper = mh.getStepper(200, 1)
	myStepper.setSpeed(60)
	stop = False
	print("Press enter to move the shade down. Press q when shade is completely down")
	count = 0
	while (stop == False):
		c = raw_input(">> ")
		if c == "q":
			stop = True
		else:
			myStepper.step(50, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
			count += 50
	return count

# function to completely roll shades up or down
def allUp(current, dest):
	steps = abs(dest - current)
	atexit.register(turnOffMotors)
	myStepper = mh.getStepper(200, 1)
	myStepper.setSpeed(50)
	myStepper.step(steps, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.MICROSTEP)

def allDown(current, dest):
	steps = abs(dest - current)
	atexit.register(turnOffMotors)
	myStepper = mh.getStepper(200, 1)
	myStepper.setSpeed(50)
	myStepper.step(steps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)

# function to roll shades up incrementally
def move_up(count):
    if (count-40) < 0:
        steps = count
    else:
        steps = 40
    atexit.register(turnOffMotors)
    myStepper = mh.getStepper(200, 1)
    myStepper.setSpeed(50)
    myStepper.step(steps, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.MICROSTEP)
    count -=steps
    print (count)


# function to roll shades up incrementally
def move_down(count, max):
    if (count+40) > max:
        steps = max - count
    else:
        steps = 40
    atexit.register(turnOffMotors)
    myStepper = mh.getStepper(200, 1)
    myStepper.setSpeed(50)
    myStepper.step(steps, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
    count += steps
    print (count)
