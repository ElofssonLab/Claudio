from __future__ import division
import sys
import numpy
import csv
import re
import pandas as pd

# filename and number of lines requested

#contact_file = sys.argv[1]
unit_file = sys.argv[1]

with open(unit_file,'r') as csv_file:
	lines = csv_file.readlines()
	

	units = []
	for line in lines:
		data = line.split(',')
		units.append(data[1:])
		#print units	
	a=0
	b=1
	for i in units: 
		print range(int(i[a]),int(i[a+1])+1)
		a=+2
		print range(int(i[a]),int(i[a+1])+1)
		continue
