import sys
import linecache
import Bio.PDB
import numpy
import csv
import pandas as pd
from os.path import expanduser
import parse_contacts


# filename and number of lines requested

TM_name = sys.argv[1]
PPV = sys.argv[2]

#c_filename = sys.argv[4]
#out= sys.argv[2]

#pdb_filename = pdb_code + ".pdb" #not the full cage!

# count the total number of lines
tot_lines = len(open(TM_name).readlines())

TM = list(linecache.getline(TM_name,24))

residues = []    
#print test
for num, val in enumerate(TM):
    if val != "-":
        residues.append(num)


res1=residues[0]
res2=residues[-1]


#PPV
contacts = parse_contacts.parse(open(PPV, 'r'))
score = [x[0] for x in contacts]
c_1 = [x[1] for x in contacts]
c_2 = [x[2] for x in contacts]

line = open(PPV,'r').readline()

for i in contacts:
    if c_1[i] <= residues[0] and c_2[i] <= residues[-1]:
    	print c_1[i], c_2[i], score[i]
    else:
        continue
