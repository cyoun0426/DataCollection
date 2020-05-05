#!/usr/bin/env python3

import os

PATH = '../user/'           # path to data directory
trip_id = 0
is_write = False

for filename in os.listdir(PATH):
    with open(PATH + filename) as f_read:
        print(filename)
        for line in f_read:
            split = line.split(',')
            if split[1] == 'label' and split[3] == 'start\n':
                f_write = open(str(trip_id) + '.csv', 'a+')
                is_write = True
                trip_id += 1
            if split[1] == 'label' and split[3] == 'end\n':
                is_write = False
                f_write.close()
            if is_write:
                f_write.write(line)
                print(line)    

