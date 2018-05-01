import os
import datetime
import time
import read_data
import control_shades

def main():
    download_dir = "temp_state.csv"
    csv = open(download_dir, "w")
    columnTitleRow = "Date, Time, amb-sat, amb-des, state, amb, sat, lock"
    csv.write(columnTitleRow)

    locked = 0
    # state 0 for close, 1 for open
    state = 0
    new_state = 0
    shade_state = 2500
    max_length = 2500
    # temp variables
    amb = 0
    sat = 0
    des_amb_diff = 0
    sat_amb_diff = 0
    # desired temperature
    des_temp = 23

    while (1):
        now = datetime.datetime.now()
        if now.hour < 6:
            locked = 1
        elif now.hour == 22:
            new_state = 1
        elif now.hour > 22:
            locked = 1
        else:
            locked = 0

        print("Collecting data")
        #collect temp and find the difference every minute for 30 minutes
        for i in range(10):
            print i
            time.sleep(60)
            amb = read_data.read_temp_a()[0]
            sat = read_data.read_temp_b()[0]
            sat_amb_diff += (amb-sat)

        print ("total: %f" %(sat_amb_diff))
        #calculate the difference between the desired and the ambient temperature
        des_amb_diff = amb - des_temp #negative want it heat up, pos cool down
        sat_amb_diff = sat_amb_diff/10.0 #negative -> has sun, pos less sun
        print("des_amb: %f sat_amb: %f" %(des_amb_diff, sat_amb_diff))
        # determine new state based on the differences
        if des_amb_diff <= -1 and sat_amb_diff <= -1:
            new_state = 1
        elif des_amb_diff > 1 and sat_amb_diff > 1:
            new_state = 0
        elif des_amb_diff > 1 and sat_amb_diff < -1:
            new_state = 0
        elif des_amb_diff < -1 and sat_amb_diff > 1:
            new_state = 1

        print("lock: %d new_state: %d state: %d" %(locked, new_state, state))
        if locked == 0 and new_state != state:
            #move shade
            print("Move shade")
            if new_state == 1:
                control_shades.allUp(shade_state, 0)
                shade_state = 0

            else:
                control_shades.allDown(shade_state, max_length)
                shade_state = max_length

	now = datetime.datetime.now()
	cur_time = str(now.hour)+":"+str(now.minute)
	date = str(now.month) + "/" + str(now.day)
        # update state of shade
        res_ls = [date, cur_time, str(sat_amb_diff), str(des_amb_diff), str(new_state), str(amb), str(sat), str(locked)]
        res_str = ", ".join(res_ls)+"\n"
        csv.write(res_str)
        state = new_state

main()
