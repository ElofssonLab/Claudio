import sys
import csv
import argparse
import pandas as pd
import numpy as np


inputfile = sys.argv[1]
sasafile1 = sys.argv[2]
sasafile2 = sys.argv[3]
corfile = sys.argv[4]
outfile = sys.argv[5]

csvVar = csv.reader(open(corfile, 'rb'))

#Accessible residues
AR = []
AR2 = []
sasr = {'residue':['ARG', 'HIS', 'LYS', 'ASP', 'GLU', 'SER', 'THR', 'ASN', 'GLN', 'CYS', 'GLY','PRO', 'ALA', 'ILE', 'LEU', 'MET', 'PHE', 'TRP', 'TYR','VAL'],
'RSA_ARNE':[225,195,200,150,190,115,140,160,180,135,75,145,115,175,170,185,210,255,230,155]}


with open(sasafile1,'r') as sa:
	df = pd.read_csv(sasafile1, sep=" ", header=None, delimiter=r"\s+")
	df2 = pd.DataFrame(sasr, columns = ['residue', 'RSA_ARNE'])
	df3 = pd.merge(df, df2, left_on=3, right_on='residue',how='inner')
	df3['exp'] = df3[5]/df3['RSA_ARNE']
	df3['ExpR'] = np.where((df3['exp']> 0.2), df3[2], np.nan)
	AR = df3['ExpR'].tolist()
with open(sasafile2,'r') as sa:
	df4 = pd.read_csv(sasafile2, sep=" ", header=None, delimiter=r"\s+")
	df5 = pd.DataFrame(sasr, columns = ['residue', 'RSA_ARNE'])
	df6 = pd.merge(df4, df5, left_on=3, right_on='residue',how='inner')
	df6['exp'] = df6[5]/df6['RSA_ARNE']
	df6['ExpR'] = np.where((df6['exp']> 0.2), df6[2], np.nan)
	AR2 = df6['ExpR'].tolist()
Acc_res = AR + AR2
print Acc_res
#PFAM_domain
for row in csvVar:
  col1, col2, col3, col4, col5 = row
  #print "%s: %s, %s, %s, %s," % (col1, col2, col3, col4, col5)

with open(inputfile,'r') as fin, open (outfile,'wb') as fout:
	writer = csv.writer(fout, delimiter=' ')       
	for row in csv.reader(fin, delimiter=' '):
			if int(row[1])-int(row[0]) >= 5:
				if int(row[0]) >= int(col2) and int(row[0]) <= int(col3):
					if int(row[1]) >= int(col4) and int(row[1]) <= int(col5):
						if int(row[1]) and int(row[0]) in Acc_res:					
							writer.writerow(row)		

