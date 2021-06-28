import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib.ticker as ticker


align = sys.argv[1] 
df = pd.read_csv(align, sep="\s*", header = 0,index_col=None)


fig, ax = plt.subplots()

f, ax = plt.subplots()
#change

#######
df = df.pivot(index='i', columns='j', values='probab',)
df1 = pd.DataFrame(index=range(1,299), columns=range(1,333)).fillna(0)

df1.update(df)
df1.replace(0, np.nan, inplace=True)
ax = sns.heatmap(df1, vmin='-15', vmax='0',cmap="nipy_spectral",cbar_kws={'label': 'E-value'},square = True)
print df

#change
Vhelices=[[5,17],[23,50],[54,86],[100,124],[137,153],[165,189],[218,246],[273,298]]
Vreentrant=[[193,213],[249,271]]

#change
Hhelices=[[2,24],[30,45],[49,73],[77,108],[141,168],[204,238],[251,265],[270,293],[306,331]]
Hreentrant=[[112,133],[173,196]]

##########

#control xlim
loop=0
print ax.get_xlim()
for start,stop in Vhelices:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.hlines([j], *ax.get_xlim(), color='blue',alpha=0.1)

for start,stop in Vreentrant:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.hlines([j], *ax.get_xlim(), color='red',alpha=0.1)

for start,stop in Hhelices:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.vlines([j], *ax.get_xlim(), color='blue',alpha=0.1)

for start,stop in Hreentrant:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.vlines([j], *ax.get_xlim(), color='red',alpha=0.1)


#change
positions_X = (1,50,100,150,200,250,300)
labels_X =("1","50","100","150","200","250","300")
plt.yticks(positions_X, labels_X)

positions_Y = (1,50,100,150,200,250,300)
labels_Y = ("1","50","100","150","200","250","300")
plt.xticks(positions_Y, labels_Y)

plt.xlabel('PSE1', fontsize = 15)
plt.ylabel('LysAB', fontsize = 15)
#1=16 in x ax

plt.savefig("Cons2_5a1s_structure_ali", dpi=600,figsize=(50,50))

plt.show()    
