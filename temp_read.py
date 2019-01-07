#!usr/bin/python3

#get data from thermometer


#create database
import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('/home/slice/compute/compost_temp/comp_read.db')
except Error as e:
    print(e)
    sys.exit("sqlite insert failed")
c = conn.cursor()

#create table
stmt = """CREATE TABLE IF NOT EXISTS temp_log (
    rec_time datetime PRIMARY KEY,
    lapse_hour INT,
    tempF FLOAT,
    tempC FLOAT,);"""
try:
    c.execute(stmnt)
    conn.commit()
except Error as e:
    print(e)
    sys.exit("sql create table failed")

# insert data into temp_log
stmnt = """INSERT INTO temp_log (
    rec_time,
    lapse_hour,
    tempF,
    tempC)
    VALUES (
    {curtime),
    {hours},
    {tf},
    {tc});""",format(
    curtime = v1,hours = v2,tf = v3,tc = v4)
try:
    c.execute(stmnt)
    conn.commit()
except:
    sys.exit("sql insert failed")

#process completed
