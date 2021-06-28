from __future__ import division
import sys
import linecache

# filename and number of lines requested
fname = sys.argv[1]
#out= sys.argv[2]

# count the total number of lines
tot_lines = len(open(fname).readlines())

P1 = list(linecache.getline(sys.argv[1],23))
S = list(linecache.getline(sys.argv[1],24))
P2 = list(linecache.getline(sys.argv[1],25))

#print S
#print P2 
#print P1
test = [item for item,x in enumerate(S) if x == ":"]
      
#print test

Identical = 0
Residues = 0
for i in test: 
    if P1[i] == P2[i]:
        Identical += 1 
        Residues += 1 
    else:
        Residues += 1
#print Identical
#print Residues
print Residues, Identical, float(Identical/Residues)

#with open(out, 'w') as f:
    #for item in test:
        #f.write("%s\n" % item)
