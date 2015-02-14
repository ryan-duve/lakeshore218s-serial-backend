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
        'host':'hicontrol.tunl.daq',
        'database':'slowcontrols',
}

#start serial
ser = serial.Serial('/dev/ttyS0',
         9600,
         parity=serial.PARITY_ODD,
         rtscts=False,
         bytesize=serial.SEVENBITS,
         stopbits=serial.STOPBITS_ONE,
         timeout=0,
         xonxoff=True,
         dsrdtr=False)

#start serial2 (Lakeshore 2)
ser2 = serial.Serial('/dev/ttyUSB1',
         9600,
         parity=serial.PARITY_ODD,
         rtscts=False,
         bytesize=serial.SEVENBITS,
         stopbits=serial.STOPBITS_ONE,
         timeout=0,
         xonxoff=True,
         dsrdtr=False)

#start mysql
cnx = mysql.connector.connect(**config) 
cur = cnx.cursor() 
