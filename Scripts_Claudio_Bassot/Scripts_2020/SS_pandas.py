import argparse
import sys
import pandas as pd
import numpy as np
from itertools import islice
import matplotlib.pyplot as plt
import glob

for name in glob.glob('*.ss'):
	#print(name)
	with open(name, 'r') as fil:
		for line in islice(fil, 0, 2):
			data = line.read().replace('\n', '')
			print(data)

