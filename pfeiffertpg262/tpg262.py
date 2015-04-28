#!/usr/bin/python

#tpg262.py
#reads pressures from Pfeiffer Dual Gauge and writes to MySQL database

import sys
import thread,time
from writeInstruments import *
from configuration import *
from pfeiffer import TPG262

#set up TPG
tpg = TPG262(port='/dev/ttyUSB2')

print "Reading pressures: press Ctrl+C to stop"
#http://ubuntuforums.org/showthread.php?t=1514035#post_9488318
try:
	while True:
		data = tpg.pressure_gauges()

		if data>0:
			writeInstruments(data,password,cur,cnx)

		time.sleep(1)
except KeyboardInterrupt:
	print "\nStopping data acquistion"

#kill mysql
cur.close()
cnx.close()
