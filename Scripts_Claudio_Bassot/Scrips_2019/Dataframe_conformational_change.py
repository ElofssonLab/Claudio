from __future__ import division
import numpy as np
import pandas as pd
import sys


P1 = sys.argv[1]
P2 = sys.argv[2]

df1 =  pd.read_csv(P1,sep=' ', names=["Res1", "Res2", "score", "Distance1"])
df2 =  pd.read_csv(P2,sep=' ', names=["Res1", "Res2", "score", "Distance2"])
df2['Distance2'].values 
df1['Distance2'] = df2['Distance2'].values
df1['Conf. Change'] = df1['Distance2'] - df1['Distance1']
#Single unit modeled with the complete region

cols = ['score']
df1[cols]= df1[df1[cols] > 0.5][cols]
df1= df1.dropna()

numOfRows = df1.shape[0]

df3 = df1.apply(lambda x: True if x['Distance1'] <= 8 and x['Distance2'] <= 8 else False , axis=1)
df4 = df1.apply(lambda x: True if (x['Distance1'] <= 8 or x['Distance2'] <= 8) and not (x['Distance1'] <= 8 and x['Distance2'] <= 8 ) else False , axis=1)
num_cor = len(df3[df3 == True].index)
num_conf = len(df4[df4 == True].index)

correct = num_cor/numOfRows
conformational_change = num_conf/numOfRows

numOfRows = df1.shape[0]

print P2, correct, conformational_change, numOfRows
