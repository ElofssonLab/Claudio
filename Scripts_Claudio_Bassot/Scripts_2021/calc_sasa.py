import pandas as pd
dfo = pd.read_csv('open.csv',delim_whitespace=True)  
dfc = pd.read_csv('closed.csv',delim_whitespace=True)
dfm = dfc.merge(dfo, on="num")

df2 =dfm[['num','SAO','SAC']]
df2.to_csv('diff_sasa.csv')
print df2

