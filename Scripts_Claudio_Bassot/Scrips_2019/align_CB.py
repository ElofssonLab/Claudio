import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO
import parse_pdb


PDB1 = sys.argv[1]
PDB2 = sys.argv[2]
chain1 = sys.argv[3]
chain2 = sys.argv[4]
out = sys.argv[5]

#extract pdb sequences
P1 = parse_pdb.get_atom_seq(open(PDB1, 'r'), chain1)
P2 = parse_pdb.get_atom_seq(open(PDB2, 'r'), chain2)
#print P1
#print P1
#print P2
#align the proteins

alignments = pairwise2.align.localms(P1, P2, 2, -1, -0.5, -0.001)  
#print alignments[0][0]
#print alignments[0][1]

#print PDB1 
#print chain1


#print Cordinates
Read = parse_pdb.read(open(PDB1, 'r'), chain1, model=1)
res_lst = Read[1]
out = open(out, 'w')
for i in  [0,1,2]:
	for j in res_lst[i]:
		print(j[:-2])

