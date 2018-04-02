import os
import time
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


temp_sensor_a = "/sys/bus/w1/devices/28-00000a45b01a/w1_slave"
temp_sensor_b = "/sys/bus/w1/devices/28-00000a46557b/w1_slave"
#We then need to define a variable for our raw temperature value (temp_raw); the two lines outputted by the sensor demonstrated with our terminal example. We could simply print this statement now. However, we’re going to process it into something more useable. So, we open, read, record and then close our temperature file. We use the return function here, in order to recall this data at a later stage in our code.

def temp_raw_a():

    f = open(temp_sensor_a, 'r')
    lines = f.readlines()
    f.close()
    return lines
def temp_raw_b():

    f = open(temp_sensor_b, 'r')
    lines = f.readlines()
    f.close()
    return lines

#First, we check our variable from the previous function for any errors. If you study our original output as defined in the terminal example, we get two lines of code (Line 0 = 72 01 4b 46 7f ff 0e 10 57 : crc=57 YES); we strip this line except for the last three digits, and check for the “YES” signal, indicating a successful temperature reading from the sensor. In Python, not-equal is defined as “!=”, so here we’re saying whilst the reading does not equal YES, sleep for 0.2s and repeat.

def read_temp_b():

    lines = temp_raw_b()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw_b()

#Once the program is happy that the YES signal has been received, we proceed to our second line of output code (Line 1 = 72 01 4b 46 7f ff 0e 10 57 t=23125). We find our temperature output “t=”, check it for errors, strip the output of the “t=” phrase to leave just the temperature numbers, and run two calculations to give us the figures in Celsius and Fahrenheit.

    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
def read_temp_a():

    lines = temp_raw_a()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw_a()

#Once the program is happy that the YES signal has been received, we proceed to our second line of output code (Line 1 = 72 01 4b 46 7f ff 0e 10 57 t=23125). We find our temperature output “t=”, check it for errors, strip the output of the “t=” phrase to leave just the temperature numbers, and run two calculations to give us the figures in Celsius and Fahrenheit.

    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
#Finally, we loop our process and tell it to output our temperature data every 1 second.

def main():
    print("Collecting data from temp sensors")
    dic = {}
    download_dir = "temp_data.csv"
    csv = open(download_dir, "w")
    columnTitleRow = "time, temp\n"
    csv.write(columnTitleRow)
    count = 0
    while count != 1440:
        local_time = time.localtime(time.time())
        key = str(local_time.tm_hour) + ":"+ str(local_time.tm_min)
        read_b = key+"b" +", ("+str(read_temp_b()[0])+","+str(read_temp_b()[1])+")\n"
        read_a = key+"a" +", ("+str(read_temp_a()[0])+","+str(read_temp_a()[1])+")\n"
        csv.write(read_b)
        csv.write(read_a)
        count += 1
        time.sleep(60)
    
main()