#!/usr/bin/env python2
import os
import datetime
import time
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')


temp_sensor_a = "/sys/bus/w1/devices/28-00000a395f5e/w1_slave"
temp_sensor_b = "/sys/bus/w1/devices/28-00000a45b01a/w1_slave"

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


def read_temp_b():

    lines = temp_raw_b()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw_b()


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


    temp_output = lines[1].find('t=')

    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
    
def collect_data():
    print("Collecting data from temp sensors")
    dic = {}
    download_dir = "temp_data.csv"
    csv = open(download_dir, "w")
    columnTitleRow = "Date, Time, Local(C), Satellite(C)"
    csv.write(columnTitleRow)
    count = 0
    while count != 3:
        now = datetime.datetime.now()
        date = str(now.month) + "/" + str(now.day)
        cur_time = str(now.hour) + ":" + str(now.minute)
        temp_a = str(read_temp_a()[0])
        temp_b = str(read_temp_b()[0])
        res_ls = [date, cur_time, temp_a, temp_b]
        res_str = ", ".join(res_ls)
        print(res_str)
        #csv.write(res_str)
        count += 1
        time.sleep(60)
#collect_data()