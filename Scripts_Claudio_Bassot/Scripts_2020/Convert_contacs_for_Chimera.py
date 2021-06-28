from __future__ import division
import sys
import linecache
import pandas as pd
import numpy as np

# filename and number of lines requested
fname, out, fasta  = sys.argv[1:]

seq = list(linecache.getline(fasta,2))
print seq
nlines = len(seq)

# count the total number of lines
tot_lines = (len(open(fname).readlines())-1)

df = pd.read_csv(sys.argv[1], names=['Res1', 'Res2', 'ss','dist'], delimiter=' ')
df2 = df.head(nlines)
df2['Res1'] = ":" + df2['Res1'].astype(str) +"@ca"
df2['Res2'] = ":" + df2['Res2'].astype(str) +"@ca"

booleanDictionary = {True: 'blue', False: 'red'}
df2 = df2.replace(booleanDictionary)
#print (df2)

df2 = df2.set_index('Res1')
#print df2

df2.to_csv(out, header=False, sep=' ')

