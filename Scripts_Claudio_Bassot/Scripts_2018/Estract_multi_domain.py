import sys
import csv
import argparse
import pandas as pd
import numpy as np

input1 = sys.argv[1]
outfile = sys.argv[2]

input_file = pd.read_csv(input1, delimiter = "	")
print input_file
df=input_file
df['pdbC'] = df['pdb'].astype(str) + df['chain']
df=input_file.groupby('pdbC')
df2 = df.filter(lambda x: len(x) > 1)
print df
df2.to_csv(outfile,sep=',')

