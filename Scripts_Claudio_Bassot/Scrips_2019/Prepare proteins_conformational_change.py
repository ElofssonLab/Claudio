import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO
from Bio.PDB import *
from Bio.PDB.Polypeptide import PPBuilder
import parse_pdb

PDB1 = sys.argv[1]
PDB2 = sys.argv[2]
chain1 = sys.argv[3]
chain2 = sys.argv[4]
out = sys.argv[5]


parser = PDBParser()


#extract pdb sequences
Cluster_rap = parser.get_structure('Cluster_rap',sys.argv[1])
P2 = parser.get_structure( 'P2',sys.argv[2])

seq1 = parse_pdb.get_atom_seq(open(sys.argv[1], 'r'), chain1)
seq2 = parse_pdb.get_atom_seq(open(sys.argv[2], 'r'), chain2)

alignments = pairwise2.align.localms(seq1, seq2, 2, -1, -0.5, -0.001)
print "Protein1 \n", alignments[0][0]
print "Protein2 \n", alignments[0][1]

list_conserved = []
gap = 0

for i, (a, b) in enumerate(zip(alignments[0][0], alignments[0][1])):
   if a != '-' and b != '-':
        list_conserved.append(i)
print list_conserved

class ResSelect(Select):
    def accept_residue(self, residue):

        if residue.id[1] in list_conserved and residue.parent.id == chain2:
            #print residue
            return True
        else:
            return False

io = PDBIO()
io.set_structure(P2)
io.save(out, ResSelect())
