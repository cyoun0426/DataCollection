#!/usr/bin/env python3

import sys
import os
import datetime
from dateutil.relativedelta import relativedelta

PATH_GPX = "./gpx/"
PATH_PLT = "./plt_manual/"

def parse(input):
    filename, date, time = input.split(' ')

    FIRST_LINES = "Geolife trajectory\nWGS 84\nAltitude is in Feet\nReserved 3\n0,2,255,My Track,0,0,2,8421376\n0"      # I kept the first 6 lines the same
    year = int(date.split('/')[0])
    month = int(date.split('/')[1])
    day = int(date.split('/')[2])
    hour = int(time.split(':')[0]) + 4
    if hour > 23:
        hour -= 24
        day += 1
    min = int(time.split(':')[1])
    DT = datetime.datetime(year, month, day, hour, min, 0)
    
    name = filename.split('.')[0]                                       # get rid of .gpx extension
    user = name.split('_')[0]
    
    # open file to write
    if not os.path.exists(PATH_PLT + user + '/'):
        os.mkdir(PATH_PLT + user + '/')
    file_w = open(PATH_PLT + user + '/' + name + ".plt", "w")
    file_w.write(FIRST_LINES)                                           # append first 6 lines

    with open(PATH_GPX + filename) as info:                             # open file to read
        for line in info:
            if '<trkpt' in line:
                latitude = line.split('"')[1]
                longitude = line.split('"')[3]

                total = relativedelta(DT, datetime.datetime(1899, 12, 30)).years
                string = latitude+','+longitude+',0,0,'+str(total)+','+DT.strftime("%Y")+'-'+DT.strftime("%m")+'-'+DT.strftime("%d")+','+DT.strftime("%X")
                file_w.write(string+'\n')
                DT += datetime.timedelta(seconds = 1)
    file_w.close()                                                      # close file to write

    
if __name__ == "__main__":
    print("Please enter: [filename.gpx] [year]/[month]/[day] [hour (24-format)]:[minute]")

    if not os.path.exists(PATH_PLT):
        os.mkdir(PATH_PLT)

    for line in sys.stdin:    
        parse(line.strip())
