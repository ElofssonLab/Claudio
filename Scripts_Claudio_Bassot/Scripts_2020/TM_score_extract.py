import sys
import linecache
import Bio.PDB
import numpy
import csv


# filename and number of lines requested

TM_name = sys.argv[1]


#c_filename = sys.argv[4]
#out= sys.argv[2]

#pdb_filename = pdb_code + ".pdb" #not the full cage!

# count the total number of lines
tot_lines = len(open(TM_name).readlines())

TM1 = linecache.getline(TM_name,24)
TM2 = linecache.getline(TM_name,26)


print ">P1"
print TM1
print ">P2"
print TM2

