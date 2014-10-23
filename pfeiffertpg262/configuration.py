#configuration.py
#set up mysql connections

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

#start mysql
cnx = mysql.connector.connect(**config) 
cur = cnx.cursor() 
