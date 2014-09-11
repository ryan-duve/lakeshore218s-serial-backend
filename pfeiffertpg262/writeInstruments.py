#writeInstruments.py
#writeInstruments takes in data tuple returned by module and writes response to database

import re
def writeInstruments(data,password,cur,cnx):
        #clean string and break into float array
	#data[0]: gauge 1, value
	#data[1][0]: gauge 1, measurement status
	#data[2]: gauge 2, value
	#data[3][0]: gauge 2, measurement status

        query = "INSERT INTO slowcontrolreadings (device, raw_reading,measurement_reading) VALUES (%s,%s,%s)"

	#instruments[0] = OVC pressure
	#instruments[1] = IVC pressure

        entries= [('IVCpressure',data[0],data[0]),('OVCpressure',data[2],data[2])]

        cur.executemany(query,entries)
        cnx.commit()
