#!/usr/bin/python
#lakeshore218s-read.py

import serial

ser = serial.Serial('/dev/ttyS0',
	 9600,
	 parity=serial.PARITY_ODD,
	 rtscts=False,
	 bytesize=serial.SEVENBITS,
	 stopbits=serial.STOPBITS_ONE,
	 timeout=5,
	 xonxoff=True,
	 dsrdtr=False)

ser.write("KRDG? 0\r\n")

print(ser.read(64))

ser.close()
