#!/usr/bin/env python3

#A simple script to read the output register of the TI
#ADS1110 ADC and spit out the raw hex value to stdout
#TI produces 8 versions of the ADS1110 each with a differnt
#buss addresses from 0x48(A0) to 0x4F(A7) 

import quick2wire.i2c as i2c
import struct
import sys

address = 0x49     # Address for ADS1110A1
config_byte = 0x8C # what to fill the config register with (default 0x8C)

with i2c.I2CMaster() as bus:
	#configure the device with a non-default config byte
	#bus.transaction(i2c.write_bytes(address, config_byte))
	
	#Pulls the values from ADC buffer 
	#only retuns values from 1st (and only)  read in trasaction
	results = bus.transaction(i2c.reading(address,2))[0]

	#Convert the string returned from read to a short intiger
	results_parse = struct.unpack(">H", results)[0]
	sys.stdout.write(hex(results_parse))

