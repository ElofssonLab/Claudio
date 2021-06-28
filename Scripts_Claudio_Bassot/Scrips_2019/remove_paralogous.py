#!/bin/env python

import sys, getopt,re

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#from Bio.SeqFeature import SeqFeature, FeatureLocation


fileA=sys.argv[1]
#Output=sys.argv[2]


handleA = open(fileA, 'rU')
handleB = open(fileA, 'rU')

dataA={}
unique={}

list_of_lines = handleB.read().splitlines()

#print "opening "+ fileA +"\n"
# For each record (mitochrodrial genome, in this case)...

for record in SeqIO.parse(handleA, 'fasta') :
    organism= re.sub(r'[\<\>\/\\\|a-z].*_','',record.name)
    organism= re.sub(r'\/.*','',organism)
    if (not organism in dataA.keys()):
#       print record.name,organism
        dataA[organism]=record

for key in dataA.keys():
    if key not in unique.keys():
        unique[key] = key

#with open(Output, 'a') as f:
print str(list_of_lines[0])
print str(list_of_lines[1])

for key in dataA.keys():
    if key in  unique.keys() and dataA[key].seq != str(list_of_lines[1]):
        print ">" + key
        print str(dataA[key].seq)
