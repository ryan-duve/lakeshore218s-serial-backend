#configuration.py
#set up serial and mysql connections

import serial
import mysql.connector

#get password
with open ("password", "r") as myfile:
    password=myfile.read().replace('\n', '')

#mysql config
#http://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
config={
        'user':'uva_remote',
        'password':password,
        'host':'hfgx620.tunl.daq',
        'database':'slowcontrols',
}

#start serial
#http://pyserial.sourceforge.net/pyserial_api.html
ser = serial.Serial('/dev/ttyUSB0',
         9600,
         parity=serial.PARITY_NONE,
         rtscts=False,
         bytesize=serial.EIGHTBITS,
         stopbits=serial.STOPBITS_ONE,
         timeout=0,
         xonxoff=False,
         dsrdtr=False)

#start mysql
cnx = mysql.connector.connect(**config) 
cur = cnx.cursor() 
