import argparse
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

features = sys.argv[1]
df = pd.read_csv(features, header = 0)
df = df.sort_values(by=['Prediction'], ascending=False)
#print(df)

# false positive rate
fpr = []
fpr2 = []
fpr3 = []
# true positive rate
tpr = []
tpr2 = []
tpr3 = []

# Iterate thresholds from 0.0, 0.01, ... 1.0
thresholds = np.arange(0.6, 0.5, 0.4)

TMscore = df['TM_score']
Prediction =df['Prediction']
# get number of positive and negative examples in the dataset
P = sum(TMscore>= 0.5)
N = len(TMscore) - P

FP=0
TP=0
for i in range(len(Prediction)):
	if TMscore[i] >= 0.5:
        	TP = TP + 1
	if TMscore[i] <= 0.5:
		FP = FP + 1
		
	fpr.append(FP/float(N))
	tpr.append(TP/float(P))


plt.plot(tpr, fpr)

plt.show()


