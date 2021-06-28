import sys
import csv, fileinput
import argparse

input1 = sys.argv[1]
outfile = sys.argv[2]

with open(input1, mode='r') as infile:
	pr = csv.reader(infile, delimiter=' ')
	res_list = [rows[0:2] for rows in pr]
with open(input1, mode='r') as infile:
	lines = infile.read().split("\n")
num_list = []
for line in lines:
    try:
        item = line.split(" ")[2]	#Choose 3th column
        num_list.append(float(item))    #Try to parse 
    except:
        pass                            #If it can't parse, the string is not a number

M=(max(num_list))                    #Prints maximum value
outlist = []
with open(input1, mode='r') as infile:
	reader = csv.reader(infile, delimiter=' ')
	for rows in reader:	
		outlist.append(float(rows[2])/M)
with open(outfile,'wb') as csvfile:
	out = csv.writer(csvfile)
	out.writerows(zip(res_list,outlist))
