import sys
import csv
import argparse
import numpy as np
import pandas as pd

Mean = []
STD = []

for filename in sys.argv[1:]:
	df = pd.read_csv(filename, delimiter = ',', header = None)
	mean = df[2].mean()
	std = df[2].std()
	Mean.append(mean)
	STD.append(std)
	
Mx = np.mean(Mean)
STDx = np.mean(STD)
print Mx
print STDx	
for filename in sys.argv[1:]:
	df = pd.read_csv(filename, delimiter = ',', header = None)
	df[3] = (df.ix[:, 2] - Mx)/STDx	
	fn = filename + '_Z'
	df1 = df
	df1.drop(df1.columns[2], axis=1, inplace=True)
	with open(fn, 'w'):	
		df1.to_csv(fn, sep=' ', header = None, index=False)
		

