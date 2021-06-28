import Bio.PDB as bpdb
import pandas as pd
import sys
import csv
import argparse
pdb = sys.argv[1]
le = sys.argv[2]
output = sys.argv[3]

 

s = bpdb.PDBParser().get_structure('temp', pdb)
io = bpdb.PDBIO()
io.set_structure(s)

df = pd.read_csv(le, sep=" |\t|\n", engine='python', names=['note', 'start', 'end', 'd', 'e',], header=None)
#file_name = row['note'] == "": 
for index, row in df.iterrows():
    if row['note'] == "UNIT": 
	print row['start'], row['end']

              #  if res.id[1] >= int(row['start']) and res.id[1] <= int(row['end']):
              #      print index
              #      with open("output{0}.pdb".format(index), 'w') as output:
	#		io.save(output, ResSelect())

class ResSelect(bpdb.Select):
    def accept_residue(self, res):
        if res.id[1] >= int(row['start']) and res.id[1] <= int(row['end']):
                print "Savoia!"
		return True
        else:
        	return False

io.save(output, ResSelect())
          #  else:
		#    continue

#

