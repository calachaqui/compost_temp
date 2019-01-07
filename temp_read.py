#!/home/slice/berryconda3/bin/python
# get data from thermometer
import sys,os,time,datetime

#os.system('modprobe w1-gpio')
#os.system('modprobe w1-gpio')
#
#temp_sensor = '/sys/bus/w1/devices/<id here>/w1_slave'
#
#def temp_raw():
#    f = open(temp_sensor, 'r')
#    lines = f.readlines()
#    f.close()
#    return lines
#
#def read_temp():
#    lines = temp_raw()
#    while lines[0].strip() [-3:] != 'YES':
#        time.sleep(0.2)
#        lines = temp_raw()
#    temp_output = lines[1].find('t=')
#    if temp_output != -1:
#        temp_string = lines[1].strip()[temp_output+2:]
#        temp_c = float(temp_string) / 1000.0
#        temp_f = temp_c * 9.0 / 5.0 + 32.0
#        return temp_c,temp_f
#
#temps = read_temp()
#v3 = temps[1]
#v4 = temps[0]

v3 = 75.555
v4 = 27.777

# create database
import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('/home/slice/compute/compost_temp/comp_read.db')
except Error as e:
    print(e)
    sys.exit("create database failed")
c = conn.cursor()

#create table
stmnt = """CREATE TABLE IF NOT EXISTS temp_log (
    rec_time CHAR(26) PRIMARY KEY,
    lapse_hour INT,
    tempF FLOAT,
    tempC FLOAT);"""
try:
    c.execute(stmnt)
    conn.commit()
except Error as e:
    print(e)
    sys.exit("sql create table failed")

# time functions
# get current time
cur_hour = datetime.datetime.now()
# get min time from database
stmnt = """select min(rec_time) FROM temp_log;"""
try:
    c.execute(stmnt)
    val = c.fetchall()
    for i in val:
        first_hour = i[0]
except:
    first_hour = datetime.datetime.now()

if first_hour == None:
    first_hour = cur_hour
    # compute hours from two times
hr_diff = cur_hour - datetime.datetime.strptime(first_hour,"%Y-%m-%d %H:%M:%S.%f")
v2 = hr_diff.seconds//3600

print(first_hour)
print(cur_hour)

# insert data into temp_log
stmnt = """INSERT INTO temp_log (
    rec_time,
    lapse_hour,
    tempF,
    tempC)
    VALUES (
    '{rec_tm}',
    {hours},
    {tf},
    {tc});""".format(
   rec_tm=cur_hour,hours=v2,tf=v3,tc=v4)
try:
    c.execute(stmnt)
    conn.commit()
except Error as e:
    print(e)
    sys.exit("sql insert failed")

#process completed
print("data inserted")
