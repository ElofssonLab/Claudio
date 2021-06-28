from __future__ import division
import sys
import linecache
import Bio.PDB
import numpy
import csv
import re
import pandas as pd
from itertools import islice


# filename and number of lines requested

Repeat_dataset = sys.argv[1]


with open(Repeat_dataset) as f:
    lines = f.readlines()
    line1 = linecache.getline(Repeat_dataset, 1)
    line2 = linecache.getline(Repeat_dataset, 2)
    line3 = linecache.getline(Repeat_dataset, 3)
    file_name = ''
    for i in range(1,9):
        file_name += str(line1[i])
   # print file_name
    p = []
    for l, c in enumerate(line3):
        if c == 'x':
            continue
        if c == '0':
            continue
        if c == '1' or c == '3' or c == '2':
            p.append(l)

  #  print p
    sequence = ''
    for a, b in enumerate(line2):
        #print b
        if a in p:
            sequence  += str(line2[a])
   # print file_name

o = open(file_name + ".fasta", "a")
o.write(">%s\n%s" % (file_name, sequence))
o.close()
