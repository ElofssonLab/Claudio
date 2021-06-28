from __future__ import division
import numpy as np
import pandas as pd
import sys


P1 = sys.argv[1]
P2 = sys.argv[2]
out = sys.argv[3]

df1 =  pd.read_csv(P1,sep=' ', names=["Res1", "Res2", "score", "Distance1"])
df2 =  pd.read_csv(P2,sep=' ', names=["Res1", "Res2", "score", "Distance2"])
df2['Distance2'].values 
df1['Distance2'] = df2['Distance2'].values
df1['Conf. Change'] = df1['Distance2'] - df1['Distance1']
#Single unit modeled with the complete region

###Filter Column ###
#cols = ['score']
#df1[cols]= df1[df1[cols] > 0.5][cols]
#df1= df1.dropna()

#numOfRows = df1.shape[0]

df1["Contact"] = np.where((df1['Distance1']<= 8) & (df1['Distance2'] <= 8), "Yes", "No")
df1["Conf_Contact"] = np.where(((df1['Distance1']<= 8) | (df1['Distance2'] <= 8)) & ~ ((df1['Distance1']<= 8) & (df1['Distance2'] <= 8)), "Yes", "No")
df1["No_contact"] = np.where((df1['Distance1']> 8) & (df1['Distance2'] > 8), "Yes", "No")

df1.loc[df1.Contact == "Yes", 'Type'] = 'Contact' 
df1.loc[df1.Conf_Contact == "Yes", 'Type'] = 'Conf_Contact' 
df1.loc[df1.No_contact == "Yes", 'Type'] = 'No_contact' 
#df1.groupby(Contact)['Type']
#df1.groupby(Conf_Contact)['Type']
#df.groupby(No_contact)['Type']

#num_cor = len(df3[df3 == True].index)
#num_conf = len(df4[df4 == True].index)

#correct = num_cor/numOfRows
#conformational_change = num_conf/numOfRows

#numOfRows = df1.shape[0]
df2 = df1[["Res1", "Res2",'score','Distance1','Distance2','Type']]
print df2
df2.to_csv(out)
