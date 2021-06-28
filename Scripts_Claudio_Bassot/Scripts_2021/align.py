import sys
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO
import parse_fasta
import parse_pdb

########## OPEN #################
P1_fasta = './7cwm.pdb'
P2_fasta = sys.argv[1]

name = sys.argv[1]
TEMPLATE = parse_pdb.get_atom_seq(open(P1_fasta, 'r'), 'A')
SEQ= parse_fasta.read_fasta(open(sys.argv[1], 'r')).values()[0][0]

with open(P1_fasta) as f:
    P1_header = f.readline()

with open(P2_fasta) as f:
    P2_header = f.readline()

alignments = pairwise2.align.localms(TEMPLATE, SEQ, 2, -1, -0.5, -0.001) 

with open(name.replace('.fasta','')+"_open_align.pir","w") as r:
    r.write(P1_header+ alignments[0][0] +"*"+ "\n" + ">P2_header"+"\n"+ alignments[0][1]+"*")

########## CLOSE #################

P3_fasta = './7jji.pdb'

TEMPLATE2 = parse_pdb.get_atom_seq(open(P3_fasta, 'r'), 'A')

with open(P3_fasta) as f:
    P3_header = f.readline()

alignments = pairwise2.align.localms(TEMPLATE2, SEQ, 2, -1, -0.5, -0.001) 

with open(name.replace('.fasta','')+"_close_align.pir","w") as r:
    r.write(P3_header+ alignments[0][0] +"*"+ "\n" + ">P2_header"+"\n"+ alignments[0][1]+"*")

