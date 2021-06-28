import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Resideus_seq_map.csv', sep=',', header = 0,index_col=0)
cmap = sns.cm.rocket_r
print df
#sns.axes_style("darkgrid")
#f, ax = plt.subplots()

ax = sns.heatmap(df, vmin=0, vmax=3,cmap='Greys')
ax.hlines([26,47,75,239,266,306], *ax.get_xlim(), color='blue',alpha=0.1)
ax.hlines([112,136,173,196], *ax.get_xlim(), color='red',alpha=0.1)
ax.vlines([33,64,83,119,239,275,302,341,433], *ax.get_ylim(), color='blue',alpha=0.1)# 1=16 in x ax
ax.vlines([154,187,372,399], *ax.get_ylim(), color='red',alpha=0.1)# 1=16 in x ax
plt.savefig("Seq_contact_map_lines.png", dpi=300)
plt.show()    
