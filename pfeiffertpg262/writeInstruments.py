#writeInstruments.py
#writeInstruments takes in data string returned by module and writes response to database

import re
def writeInstruments(data,password,cur,cnx):
        #clean string and break into float array
        data=re.sub(r'\+', '',data)
        instruments = data.split(",")

        query = "INSERT INTO pfeiffertpg262 (device, raw_reading) VALUES (%s,%s)"

	#instruments[0] = OVC pressure
	#instruments[1] = IVC pressure

        entries= [('OVCpressure',instruments[0]),('IVCpressure',instruments[1])]

        cur.executemany(query,entries)
        cnx.commit()
