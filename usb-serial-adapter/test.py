#!/usr/bin/python

#pfeiffertpg262.py
#reads temps from Pfeiffer Dual Gauge and writes to MySQL database

import sys
import thread,time
from writeInstruments import *
from configuration import *

print "Reading pressures: press Ctrl+C to stop"
#http://ubuntuforums.org/showthread.php?t=1514035#post_9488318
try:
	while True:
		data=ser.read(ser.inWaiting())

		if len(data)>0:
			#writeInstruments(data,password,cur,cnx)
			print 'len(data)=',len(data);

		time.sleep(1)
		ser.write("PR1\r\n")
except KeyboardInterrupt:
	print "\nStopping data acquistion"

#kill mysql
cur.close()
cnx.close()
