import sys
import csv
import argparse

input1 = sys.argv[1]
input2 = sys.argv[2]
outfile = sys.argv[3]
with open(input1, mode='r') as infile:
	reader = csv.reader(infile, delimiter=',')
	dic_gDCA = {tuple(rows[0:2]):float(rows[2]) for rows in reader}

with open(input2, mode='r') as infile:
	reader = csv.reader(infile, delimiter=',')
	dic_plmDCA = {tuple(rows[0:2]):float(rows[2]) for rows in reader}
common_keys = list(set(dic_gDCA.keys()).intersection(set(dic_plmDCA.keys())))
outgDCA = []
outplmDCA = []
for i in range(len(common_keys)):
	curr_key = common_keys[i];
	outgDCA.append(dic_gDCA[curr_key])
	outplmDCA.append(dic_plmDCA[curr_key])
def function(outgDCA,outplmDCA):
	maxscore = [max(value) for value in zip(outgDCA,outplmDCA)]
	return maxscore
with open(outfile,'wb') as csvfile:
	out = csv.writer(csvfile)
   	out.writerows(zip(common_keys, function(outgDCA,outplmDCA)))
