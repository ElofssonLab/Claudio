import pandas
import numpy as np
import sys
import linecache
import parse_contacts
import itertools
from parsing import parse_contacts


SS = sys.argv[1]
c_lst = parse_contacts.parse(open(sys.argv[2], 'r'))
out = sys.argv[3]

tot_lines = len(open(SS).readlines())
seq = list(linecache.getline(SS,2))
rang = []
for i ,c in enumerate(seq):
	#print(c)
	if (seq[i] == '1' and seq[i+1] =='2' ) or (seq[i] == '2' and seq[i+1] =='1'):	
		rang.append(i+1)
		rang.append(i+2)
	if seq[i] == '3' and seq[i-1] == '1':
		continue
		if seq[i] == '3':
			continue
			if seq[i] == '1':
				break
				if seq[i] == '2':
					rang.append(i+1)
					rang.append(i+2)
				
	if seq[i] == '3' and seq[i-1] == '2':
		continue
		if seq[i] == '3':
			continue
			if seq[i] == '2':
				break
				if seq[i] == '1':
					rang.append(i+1)
					rang.append(i+2)

rang.append(1)
rang.append(len(seq)-1)
rang.sort()
print(rang)

units = ([(rang[i],rang[i+1]) for i in range(0,len(rang),2)])

#print(units)

c_filt = []
for c in c_lst:
	score = c[0]
	res1 = c[1]
	res2 = c[2]
	for unit in units:
		start = unit[0]
		end = unit[1]
		if not (res1 >= start and res2 <= end) and (res1 <= end and res2 >= start):
			#print('%d - %d: %f in %d - %d' % (res1, res2, score, start, end))
			#print(unit)
			c_filt.append((score, res1, res2))
#print c_filt

cfilt_file = open(out, 'w')
parse_contacts.write(c_filt, cfilt_file)
cfilt_file.close()


