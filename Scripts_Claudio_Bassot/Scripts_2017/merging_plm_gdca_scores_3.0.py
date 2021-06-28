import sys
import csv
import argparse

input1 = sys.argv[1]
input2 = sys.argv[2]
outfile = sys.argv[3]
with open(input1, mode='r') as infile:
	reader = csv.reader(infile, delimiter=' ')
	dic_gDCA = {tuple(rows[0:2]):float(rows[2]) for rows in reader}

with open(input2, mode='r') as infile:
	reader = csv.reader(infile, delimiter=',')
	dic_plmDCA = {tuple(rows[0:2]):float(rows[2]) for rows in reader}

common_keys = list(set(dic_gDCA.keys()).intersection(set(dic_plmDCA.keys())))
outlist = []
for i in range(len(common_keys)):
		curr_key = common_keys[i];
		if curr_key > 0:
			outlist.append(dic_gDCA[curr_key] * dic_plmDCA[curr_key])
r_outl = [round(elem, 4) for elem in outlist]

with open(outfile,'wb') as csvfile:
	out = csv.writer(csvfile)
   	out.writerows(zip(common_keys, r_outl))
  

