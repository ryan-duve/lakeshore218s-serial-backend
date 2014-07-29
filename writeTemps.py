#writeTemps.py
#writeTemps takes in data string returned by module and writes temperatures to database

import re
def writeTemps(data,password,cur,cnx):
        #clean string and break into float array
        data=re.sub(r'\+', '',data)
        temps = data.split(",")

        query = "INSERT INTO lakeshore218s1 (device, raw_reading) VALUES (%s,%s)"

	#temps[0] = separator Si diode
	#temps[1] = evaporator Si diode
	#temps[2] = mixing chamber Si diode
        entries= [('sepSi',temps[0]),('evapSi',temps[1]),('mcSi',temps[2])]

        cur.executemany(query,entries)
        cnx.commit()
