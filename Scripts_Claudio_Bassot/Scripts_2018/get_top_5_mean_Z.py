import sys
import csv
import argparse
import numpy as np
import pandas as pd

Mean_True = []
Mean_False = []
Top_True = []
Top_False = []

for filename in sys.argv[1:]:
	df = pd.read_csv(filename, delimiter = ' ', header = None)
	try:
		means = df.groupby([3])[2].mean()
		Mean_True.append(means.loc[True])
		Mean_False.append(means.loc[False])
		
		df2 = df.groupby(3)[2].nlargest(5).mean(level=0)	
		Top_True.append(df2.loc[True])
		Top_False.append(df2.loc[False])
	except KeyError:
		continue

print np.mean(Mean_True)
print np.mean(Mean_False)
print np.mean(Top_True)
print np.mean(Top_False)




