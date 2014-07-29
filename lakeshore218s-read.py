#!/usr/bin/python
#lakeshore218s-read.py

import serial
import sys
import mysql.connector
import thread,time
import re

ser = serial.Serial('/dev/ttyS0',
	 9600,
	 parity=serial.PARITY_ODD,
	 rtscts=False,
	 bytesize=serial.SEVENBITS,
	 stopbits=serial.STOPBITS_ONE,
	 timeout=0,
	 xonxoff=True,
	 dsrdtr=False)

ser.write("KRDG? 0\r\n")
print(ser.read(64))

#**********
#loops
#http://ubuntuforums.org/showthread.php?t=1514035#post_9488318
print "Reading temperatures: press Ctrl+C to stop"

try:
	while True:
		data=ser.read(ser.inWaiting())

		if len(data)>0:
			#strip non-alphanumerics
			data=re.sub(r'\+', '',data)

			temps = data.split(",")

			sepSi = temps[0]
			evapSi = temps[1]
			mcSi = temps[2]

			print sepSi, evapSi, mcSi
		time.sleep(1)
		ser.write("KRDG? 0\r\n")
except KeyboardInterrupt:
	print "\nStopping data acquistion"

#**********

#mysql database stuff

#get password from file
with open ("password", "r") as myfile:
    password=myfile.read().replace('\n', '')

#http://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
config={
	'user':'uva_remote',
	'password':password,
	'host':'hfgx620.tunl.daq',
	'database':'slowcontrols',
}

cnx = mysql.connector.connect(**config)
cur = cnx.cursor()

query = "INSERT INTO lakeshore218s1 (device, raw_reading) VALUES (%s,%s)"
data = [('test1',1.0),('test2',2.0)]

cur.executemany(query,data)
cnx.commit()

cur.close()
cnx.close()

