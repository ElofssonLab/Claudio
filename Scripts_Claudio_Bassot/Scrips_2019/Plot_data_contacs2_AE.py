import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Resideus_seq_map.csv', sep=',', header = 0,index_col=0)
cmap = sns.cm.rocket_r
#print (df)
#sns.axes_style("darkgrid")
f, ax = plt.subplots()

ax = sns.heatmap(df, vmin=0, vmax=3,cmap='Greys')


Hhelices=[[4,23],[30,44],[55,70],[76,107],[141,168],[203,235],[250,265],[270,294],[305,330]]
Hreentrant=[[112,137],[173,196]]
#ax.hlines([26,47,75,239,266,306], *ax.get_xlim(), color='blue',alpha=0.1)
#ax.hlines([112,136,173,196], *ax.get_xlim(), color='red',alpha=0.1)
Vhelices=[[13,29],[33,56],[66,81],[100,117],[121,151],[189,222],[249,274],[284,300],[303,333],[344,370],[400,433]]
Vreentrant=[[154,187],[372,399]]
#ax.vlines([33,64,83,119,239,275,302,341,433], *ax.get_ylim(), color='blue',alpha=0.1)# 1=16 in x ax
#ax.vlines([154,187,372,399], *ax.get_ylim(), color='red',alpha=0.1)# 1=16 in x ax

loop=0
for start,stop in Hhelices:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.hlines([j], *ax.get_xlim(), color='blue',alpha=0.1)

for start,stop in Hreentrant:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.hlines([j], *ax.get_xlim(), color='red',alpha=0.1)

for start,stop in Vhelices:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.vlines([j], *ax.get_xlim(), color='blue',alpha=0.1)

for start,stop in Vreentrant:
    start+=loop
    stop+=-loop
    for j in range(start,stop):
        ax.vlines([j], *ax.get_xlim(), color='red',alpha=0.1)


#1=16 in x ax
plt.savefig("Seq_contact_map_lines.png", dpi=300)
plt.show()    
