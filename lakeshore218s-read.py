#!/usr/bin/python

#lakeshore218s-read.py
#reads temps from Lakeshore 218s and writes to MySQL database

import sys
import re
import thread,time
from writeTemps import *
from configuration import *

print "Reading temperatures: press Ctrl+C to stop"
#http://ubuntuforums.org/showthread.php?t=1514035#post_9488318
try:
	while True:
		data=ser.read(ser.inWaiting())+ser2.read(ser2.inWaiting())#Lakeshore 1
		data=data.replace("\r\n",",",1)
		#now data looks like'+295.40,+295.05,+294.28,+505.00,+00.000,+00.000,+00.000,+00.000,+295.56,+00.000,+00.000,+00.000,+00.000,+00.000,+00.000,+00.000\r\n'

		if len(data)>0:
			writeTemps(data,password,cur,cnx)

		time.sleep(1)
		ser.write("KRDG? 0\r\n")#Lakeshore 1
		ser2.write("KRDG? 0\r\n")#Lakeshore 2
except KeyboardInterrupt:
	print "\nStopping data acquistion"

#kill mysql
cur.close()
cnx.close()
