#writeTemps.py
#writeTemps takes in data string returned by module and writes temperatures to database

import re
def writeTemps(data,password,cur,cnx):
        #clean string and break into float array
        data=re.sub(r'\+', '',data)
        temps = data.split(",")

        query = "INSERT INTO slowcontrolreadings (device, raw_reading, measurement_reading) VALUES (%s,%s,%s)"

	#temps[0] = separator Si diode
	#temps[1] = evaporator Si diode
	#temps[2] = mixing chamber Si diode
        entries= [('sepSiHi',temps[0],temps[0]),('sepSiLo',temps[1],temps[1]),('mcSi',temps[2],temps[2])]

        cur.executemany(query,entries)
        cnx.commit()
