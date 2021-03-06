#!/usr/bin/env python3

import os
import datetime
from dateutil.relativedelta import relativedelta

PATH_GPX = "./gpx/"
PATH_PLT = "./plt/"

def parse(filename):

    FIRST_LINES = "Geolife trajectory\nWGS 84\nAltitude is in Feet\nReserved 3\n0,2,255,My Track,0,0,2,8421376\n0"      # I kept the first 6 lines the same
    DT = datetime.datetime(2020, 3, 16, 12, 0, 0)           # An arbitrary start date for the trips
    
    name = filename.split('.')[0]                           # get rid of .gpx extension
    
    # set date and time
    user = name.split('_')[0]
    week = name.split('_')[1]
    day = name.split('_')[2]
    tripid = name.split('_')[3]
    offset = 0
    if day == 'tue':
        offset = 1
    elif day == 'wed':
        offset = 2
    elif day == 'thu':
        offset = 3
    elif day == 'fri':
        offset = 4
    DT += datetime.timedelta(days = int(week)*7+offset)
    DT += datetime.timedelta(hours = int(tripid))
    
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
    if not os.path.exists(PATH_PLT + user + '/'):
        os.mkdir(PATH_PLT + user + '/')
    
    for filename in os.listdir(PATH_GPX):
        parse(filename)
