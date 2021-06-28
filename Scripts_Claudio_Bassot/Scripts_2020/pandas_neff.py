import pandas as pd

headers = ['id','PPV','Neff']
headers2 = ['id','PPV_DMSA']
df1 = pd.read_csv("DMP_Neff.csv", delimiter=',', names=headers)
df2 = pd.read_csv("PPV_score_DMP_DMSA", delimiter=',', names=headers2)

df3 = pd.concat([df1.set_index('id'),df2.set_index('id')], axis=1, join='inner')

df3.to_csv('MSA_vs_DMP_MSA.csv', sep = ',')  
print df3
