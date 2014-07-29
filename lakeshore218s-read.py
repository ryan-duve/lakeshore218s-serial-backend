#!/usr/bin/python

#lakeshore218s-read.py
#reads temps from Lakeshore 218s and writes to MySQL database

import sys
import thread,time
from writeTemps import *
from configuration import *

print "Reading temperatures: press Ctrl+C to stop"
#http://ubuntuforums.org/showthread.php?t=1514035#post_9488318
try:
	while True:
		data=ser.read(ser.inWaiting())

		if len(data)>0:
			writeTemps(data,password,cur,cnx)

		time.sleep(1)
		ser.write("KRDG? 0\r\n")
except KeyboardInterrupt:
	print "\nStopping data acquistion"

#kill mysql
cur.close()
cnx.close()
